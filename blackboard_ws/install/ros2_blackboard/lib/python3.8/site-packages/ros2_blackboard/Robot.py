from enum import Enum
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseWithCovarianceStamped
from message_pkg.msg import TaskMsg
from message_pkg.msg import BBbackup
from message_pkg.msg import TaskCost
from message_pkg.msg import TaskStateMsg
from std_msgs.msg import String

from ros2_blackboard.Blackboard import Blackboard
from ros2_blackboard.Controller import Controller
from ros2_blackboard.Task import Task, TaskState

from threading import Lock, Thread, current_thread
import math

class RobotState(Enum):
    busy = 0
    defect = 1
    idle = 2

class Robot(Node):
    def __init__(self, bbAdress, backupAdress, robotId, robotType, repeatability, accuracy, payload, maxVelLinear, maxVelAngular, battery, nodeName, talker, bb):
        super().__init__('robot')
        self.talker = talker
        self.bb = bb
        self.bbAdress = bbAdress
        self.buAdress = backupAdress
        self.robotId = robotId
        self.robotType = robotType

        self.repeatability = repeatability
        self.accuracy = accuracy
        self.payload = payload
        self.maxVelLiniear = maxVelLinear
        self.maxVelAngular = maxVelAngular

        self.battery = battery
        self.state = RobotState.idle
        self.nodeName = nodeName
        self.bbState = True
        self.currentTaskList = []
        self.currentTaskid = 0
        self.taskCounter = -1
        self.currentTask = None
        self.amclx = 0
        self.amcly = 0

        
        self.controller = Controller(nodeName)
        self.taskBCSub = self.create_subscription(TaskMsg, '/taskBC', self.getTaskCost, 1)
        self.taskAssignSub = self.create_subscription(TaskMsg, '/taskAssign', self.addTask, 1)
        amclPose = '/'+self.nodeName+'/amcl_pose'
        self.amclPoseSub = self.create_subscription(PoseWithCovarianceStamped, amclPose, self.initialPose, 1)
        self.bbBackupSub = self.create_subscription(BBbackup, '/bbBackup', self.bbBackup, 1)

        self.pingTimer = self.create_timer(5, self.checkBlackboardStatus)
        self.bbBackupTimer = self.create_timer(3, self.bbBackupActivate)
        self.exeTimer = self.create_timer(1, self.executeTask)

        self.lock = Lock()
        self.execLock = Lock()
        self.addtaskLock = Lock()
        self.taskCostLock = Lock()
        self.updateLock = Lock()
        self.pingLock = Lock()
        self.bbactivateLock = Lock()

    def initialPose(self, data):
        if self.taskCostLock.locked() is False:
            self.amclx = data.pose.pose.position.x
            self.amcly = data.pose.pose.position.y
    
    def bbBackup(self,data):
        if self.lock.locked() is False:
            self.lock.acquire()
            self.bbAdress = data.bbAdress
            self.buAdress = data.buAdress
            self.bbState = True
            self.lock.release()

    def addTask(self, data):
        if self.addtaskLock.locked() is False:
            self.addtaskLock.acquire()
            if data.robotId is self.robotId:
                self.newtask = Task(data.taskId, data.priority, data.taskType, data.pose, data.payload)
                self.newtask.cost = data.cost
                self.newtask.energyCost = data.energyCost
                self.newtask.taskState = TaskState.Assigned

                counter = 0                                         #Stores the index of the current list item
                for t in self.currentTaskList:
                    if t.priority < self.newtask.priority:
                        if t.taskState is TaskState.Assigned:
                            self.currentTaskList.insert(counter, self.newtask)
                            return
                    counter = counter + 1
                self.currentTaskList.append(self.newtask)
                self.taskCounter = self.taskCounter + 1
            self.addtaskLock.release()

    def getTaskCost(self, data):
        print(data)
        if self.taskCostLock.locked() is False:
            self.taskCostLock.acquire()
            cost = 1000
            cr = 10
            energyTolerance = 10
            energyAtTask = 0
            preTasks = 1

            if data.payload > self.payload:
                self.updateBlackboard(self.robotId, data.taskId, cost, 0)
                print('First exception')
                self.taskCostLock.release()
                return
            
            x = self.amclx
            y = self.amcly
            distance = -1

            for pos in data.pose:
                distance = distance + (math.sqrt((pos.position.x - x)**2) + math.sqrt((pos.position.y - y)**2))
                x = pos.position.x
                y = pos.position.y
            

            fr = cr * (data.payload + self.payload)
            en = fr * distance

            energyCost = en / self.battery.getVolt()
            print(self.nodeName, '      Distance:', distance, '      Energy:', energyCost)

            if energyCost >= self.battery.getAmps()/energyTolerance:
                cost = 1000
                self.updateBlackboard(self.robotId, data.taskId, cost, 0)
                print('second exception')
                self.taskCostLock.release()
                return
            
            for t in self.currentTaskList:
                if t.priority >= data.priority:
                    energyAtTask = energyAtTask + t.energyCost
                    preTasks = preTasks + 1
            energyAtTask = self.battery.getAmps() - energyAtTask

            if energyAtTask <= energyTolerance:
                cost = 1000
                self.updateBlackboard ( self.robotId, data.taskId, cost, 0)
                print('third exception')
                self.taskCostLock.release()
                return
            if energyAtTask != 0:
                cost = energyCost * preTasks / energyAtTask
            self.updateBlackboard(self.robotId,data.taskId,cost,energyCost)

            self.taskCostLock.release()
        
    
    def updateBlackoard(self, robotId, taskId, taskCost, energyCost):
        if self.updateLock.locked() is False:
            self.updateLock.acquire()
            tskCst = TaskCost()
            tskCst = TaskCost()                       
            tskCst.robotId = robotId            
            tskCst.taskId = taskId
            tskCst.taskCost = taskCost
            tskCst.energyCost = energyCost
            self.talker.pub_taskCost.publish(tskCst)   
            self.updateLock.release()
    
    def executeTask(self):
        if self.taskCounter >= 0:
            statemsg = TaskStateMsg()
            if self.execLock.locked() is False:
                self.execLock.acquire()

                if self.state is RobotState.idle:
                    for tasks in self.currentTaskList:
                        if tasks.taskState is TaskState.Assigned:
                            self.currentTask = tasks
                            break

                if self.state is RobotState.idle:
                    if self.currentTask.taskState is not TaskState.Done:
                        self.state = RobotState.busy
                        statemsg.taskId = self.currentTask.taskId
                        statemsg.taskState = 1
                        self.currentTask.taskState = TaskState.Started
                        self.talker.pub_taskState.publish(statemsg)
                        self.controller.startExecute(self.currentTask)
                
                if self.controller.state == 1:
                    if self.state is RobotState.busy:
                        statemsg.taskId = self.currentTask.taskId
                        statemsg.taskState = 2
                        self.currentTask.taskState = TaskState.Done
                        self.talker.pub_taskState.publish(statemsg)
                        self.battery.updateLevel(self.currentTask.energyCost)
                        self.state = RobotState.idle
                
                self.execLock.release()

    
    def setState(self,state):
        self.state = state

    def checkBlackboardStatus(self):
        if self.pingLock.locked() is False:
            self.pingLock.acquire()
            nodesList = self.get_node_names()
            if ("blackboard" not in nodesList):
                self.bbthread = Thread(target=self.bbBackupActivate)
            self.pingLock.release()
    
    def bbBackupActivate(self):
        if self.bbactivateLock.locked() is False:
            self.bbactivateLock.acquire()
            if self.bbState is False:
                if self.nodeName == self.buAdress:
                    self.bbState = True
                    self.pingTimer.shutdown()
                    self.oldbbadress = self.bbAdress
                    self.bb = Blackboard(1, self.talker)

                    if self.nodeName == 'robot1':
                        self.bb.robotnr = 4
                        self.bb.buAdress = 'robot2'

                    if self.nodeName == 'robot2':
                        self.bb.robotnr = 3
                        self.bb.buAdress = 'robot3'
                    
                    if self.nodeName == 'robot3':
                        self.bb.robotnr = 2
                        self.bb.buAdress = 'robot4'

                    if self.nodeName == 'robot4':
                        self.bb.robotnr = 1
                        self.bb.buAdress = 'robot4'

            self.bbactivateLock.release()
                




            
                

        