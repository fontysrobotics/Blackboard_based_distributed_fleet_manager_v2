from rclpy.action import ActionClient
from ros2_blackboard.Task import *
from threading import Thread
from geometry_msgs.msg import PoseStamped
from move_base_msgs.action import MoveBase

class MoveBaseCommand(Node):
    def __init__(self, robotid):
        super().__init__('movebasecommand')
        self.robotid = robotid
        moveBaseTopic = "robot" + str(self.robotid)+"/move_base"
        self.client = ActionClient(
            self, MoveBase, moveBaseTopic)
        self.client.wait_for_server()
        self.state = 0
    
    def sendGoal(self, goal):
        movebasegoal = MoveBase.Goal()
        movebasegoal.goal_pose.header.frame_id = "map"
        movebasegoal.goal_pose.header.stamp = self.get_clock().now()    #time stamp, moment of sending the goal
        movebasegoal.goal_pose.pose.position.x = goal.position.x
        movebasegoal.goal_pose.pose.position.y = goal.position.y
        movebasegoal.goal_pose.pose.orientation.w = 1.0
        self.client.send_goal(movebasegoal)

class Controller(Node):
    def __init__(self, robotid):
        super().__init__('controller')
        self.stepcounter = 0
        self.robotid = robotid
        self.mb = MoveBaseCommand(robotid)
        self.state = 0

    def startExecute(self, task):
        a = Thread(target=self.executeTask, args=(task,))
        a.start()

    def executeTask(self, task):
        self.state = -1
        self.stepcounter = 0
        task.analyzeTask()

        for step in task.stepsList:
            self.mb.sendGoal(step.pose)
            wait = self.mb.client.wait_for_result()
            if wait:
                self.stepcounter = self.stepcounter + 1

        if self.stepcounter == len(task.stepsList):
            task.taskState = TaskState.Done
            self.state = 1
