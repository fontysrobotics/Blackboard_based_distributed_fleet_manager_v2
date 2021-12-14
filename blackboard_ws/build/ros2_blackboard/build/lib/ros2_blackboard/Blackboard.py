from rclpy.node import Node
from ros2_blackboard.Task import Task, TaskState
from std_msgs.msg import String
from message_pkg.msg import TaskMsg, TaskCost, TaskStateMsg, BBsynch, BBbackup


class Blackboard(Node):
    def __init__(self, state, talker):
        super().__init__('blackboard')
        self.state = state
        self.talker = talker
        self.robotnr = 4

        if state == 1:
            self.taskList = []
            self.buAdress = 'robot1'       #change to a list based on processing resources

            #Topic subscribers
            self.newTaskSub = self.create_subscription(TaskMsg, 'newTask', self.addTask, 1)
            self.taskCostSub = self.create_subscription(TaskCost, 'taskCost', self.processTaskCost, 1)
            self.taskStateSub = self.create_subscription(TaskStateMsg, 'taskStateMsg', self.taskStateUpdate, 1)
            

            self.bbBackuptimer = self.create_timer(1, self.bbBackup)
            self.syncTimer = self.create_timer(2, self.bbsynch)

            print('new blackboard object created')

    #logs data from subscribtions 
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

    #TaskStateMsg data received --> Callback used to update task state via robots
    def taskStateUpdate(self, data):
        print(data)                                             #REMOVE -> Testing purposes
        for t in self.taskList:
            if t.taskId == data.taskid:
                if data.taskstate == 1:
                    t.taskState = TaskState.Started
                if data.taskstate == 2:
                    t.taskState = TaskState.Done
            print("taskstate: "+ t.taskState.name)
            


    #self.syncTimer callback used to syncronize the current taskList with backup blackboard, and taskview
    def bbsynch(self):
        syncarray = []
        sync = BBsynch()
        for task in self.taskList:
            tmsg = TaskMsg()
            tmsg.taskid = task.taskId
            tmsg.priority = task.priority
            tmsg.tasktype = task.taskType
            tmsg.payload = task.payload
            tmsg.taskstate = task.taskState.value
            tmsg.pose = task.pose
            tmsg.robotid = task.robotId
            syncarray.append(tmsg)
        sync.tasks = syncarray
        self.talker.pub_bbSync.publish(sync)


    #newTask data received --> callback checks for task and broadcasts it
    def addTask(self, data):
        print(data)                                           #REMOVE -> Testing purposes
        id = data.taskid
        for t in self.taskList:
            if t.taskId is id:
                break
        tsk = Task(data.taskid, data.priority, data.tasktype, data.pose, data.payload)
        self.taskList.append(tsk)
        self.broadcastTask(tsk)


    #broadcast a task over the 'taskBC' topic to subscribed robots
    def broadcastTask(self, task):
        tmsg = TaskMsg()
        tmsg.taskid = task.taskId
        tmsg.priority = task.priority
        tmsg.tasktype = task.taskType
        tmsg.payload = task.payload
        tmsg.taskstate = task.taskState.value
        tmsg.pose = task.pose
        self.talker.pub_taskBC.publish(tmsg)


    #Callback triggered by the taskCost topic. 
    def processTaskCost(self, data):
        print(data)                                          #REMOVE -> Testing purposes
        for t in self.taskList:
            if t.taskId == data.taskid:
                if t.cost >= data.taskcost:
                    t.robotId = data.robotid
                    t.cost = data.taskcost
                    t.energyCost = data.energycost
                t.receivedCosts = t.receivedCosts+1
            if t.receivedCosts == self.robotnr:
                self.assignTask(t)
        
    

    #Converts a task object to custom ROS message and publishes over 'taskAssign' topic
    def assignTask(self, task):
        if task.taskstate is TaskState.Waitting:
            tmsg = TaskMsg()
            tmsg.robotid = task.robotId
            tmsg.taskid = task.taskId
            tmsg.priority = task.priority
            tmsg.tasktype = task.taskType
            tmsg.payload = task.payload
            tmsg.taskstate = task.taskState.value
            tmsg.pose = task.pose
            tmsg.cost = task.cost
            tmsg.energycost = task.energyCost
            task.taskstate = TaskState.Assigned
            self.talker.pub_taskAssign.publish(tmsg)
    

    #Ros timer callback broadcasts current blackboard and backup adresses
    def bbBackup(self, event=None):
        bumsg = BBbackup()
        bumsg.bbadress = self.talker.nodeName
        bumsg.buadress = self.buAdress
        self.talker.pub_bbBackup.publish(bumsg)
