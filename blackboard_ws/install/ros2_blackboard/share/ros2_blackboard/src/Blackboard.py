import rclpy
from rclpy.node import Node
from blackboard.Task import Task, TaskState
from std_msgs.msg import String
from message_pkg.msg import TaskMsg, TaskCost, BBbackup, BBsynch, TaskStateMsg

class Blackboard(Node):
    def __init__(self, state, talker):
        self.state = state
        self.talker = talker
        self.robotnr = 4

        if state == 1:
            self.taskList = []
            self.buAdress = 'robot1'       #change to a list based on processing resources

            #Topic subscribers
            Node.create_subscription(self, TaskMsg, 'newTask', self.addTask, 1)
            Node.create_subscription(self, TaskCost, 'taskCost', self.processTaskCost, 1)
            Node.create_subscription(self, TaskStateMsg, 'taskStateMsg', self.taskStateUpdate, 1)

            self.bbBackuptimer = self.create_timer(1, self.bbBackup)
            self.syncTimer = self.create_timer(2, self.bbsynch)

            print('new blackboard object created')


    #TaskStateMsg data received --> Callback used to update task state via robots
    def taskStateUpdate(self, data):
        for t in self.taskList:
            if t.taskId == data.taskId:
                if data.taskState == 1:
                    t.taskState = TaskState.Started
                if data.taskState == 2:
                    t.taskState = TaskState.Done


    #self.syncTimer callback used to syncronize the current taskList with backup blackboard, and taskview
    def bbsynch(self, event):
        syncarray = []
        sync = BBsynch()
        for task in self.taskList:
            tmsg = TaskMsg()
            tmsg.taskId = task.taskId
            tmsg.priority = task.priority
            tmsg.taskType = task.taskType
            tmsg.payload = task.payload
            tmsg.taskState = task.taskState.value
            tmsg.pose = task.pose
            tmsg.robotId = task.robotId
            syncarray.append(tmsg)
        sync.tasks = syncarray
        self.talker.pub_bbSync.publish(sync)


    #newTask data received --> callback checks for task and broadcasts it
    def addTask(self, data):
        id = data.taskId
        for t in self.taskList:
            if t.taskId is id:
                break
        tsk = Task(data.taskId, data.priority, data.taskType, data.pose, data.payload)
        self.taskList.append(tsk)
        self.broadcastTask(tsk)


    #broadcast a task over the 'taskBC' topic to subscribed robots
    def broadcastTask(self, task):
        tmsg = TaskMsg()
        tmsg.taskId = task.taskId
        tmsg.priority = task.priority
        tmsg.taskType = task.taskType
        tmsg.payload = task.payload
        tmsg.taskState = task.taskState.value
        tmsg.pose = task.pose
        self.talker.pub_taskBC.publish(tmsg)


    #Callback triggered by the taskCost topic. 
    def processTaskCost(self, data):
        for t in self.taskList:
            if t.taskId == data.taskId:
                if t.cost >= data.taskCost:
                    t.robotId = data.robotId
                    t.cost = data.taskCost
                    t.energyCost = data.energyCost
                t.receivedCosts = t.receivedCosts+1
            if t.receivedCosts == self.robotnr:
                self.assignTask(t)
    

    #Converts a task object to custom ROS message and publishes over 'taskAssign' topic
    def assignTask(self, task):
        if task.taskState is TaskState.Waitting:
            tmsg = TaskMsg()
            tmsg.robotId = task.robotId
            tmsg.taskId = task.taskId
            tmsg.priority = task.priority
            tmsg.tasktype = task.taskType
            tmsg.payload = task.payload
            tmsg.taskState = task.taskState.value
            tmsg.pose = task.pose
            tmsg.cost = task.cost
            tmsg.energyCost = task.energyCost
            task.taskState = TaskState.Assigned
            self.talker.pub_taskAssign.publish(tmsg)
    

    #Ros timer callback broadcasts current blackboard and backup adresses
    def bbBackup(self, event=None):
        bumsg = BBbackup()
        bumsg.bbAdress = self.talker.nodeName
        bumsg.buAdress = self.buAdress
        self.talker.pub_bbBackup.publish(bumsg)
