import unittest
from enum import Enum


# task types enum
class TaskType(Enum):
    GA = 1                  # go to position a
    GAB = 2                 # go to position a then b
    GPA = 3                 # go to position a and pick object
    GPAB = 4                # go to position a pick then go to pose b


# task state enums
class TaskState(Enum):
    Waitting = 0
    Started = 1
    Done = 2
    Assigned = 3


# start task class
class Task():
    # initilize a task object with the passed parameters
    def __init__(self,taskID,
                 priority,
                 taskType, 
                 pose,  
                 payload):

        self.taskId=taskID
        self.priority = priority
        self.taskType = taskType
        self.pose = pose
        self.payload = payload
        self.taskState = TaskState.Waitting     # when task is created its in waitting state
        self.cost = 1000                        # cost is set to max to be adjusted when calculated later
        self.energyCost = 0                     # amps used to execute task, added to simulate battery usage
        self.robotId = -1                       # task is not assigned " robot id -1 does not exist "
        self.receivedCosts = 0                   # number of recived costs from robots 
        self.stepsList = []                     # a list to hold task steps when a task is analyzed
    
    def taskToString(self, tsk):
        stt = ''
        if tsk.taskState == TaskState.Waitting:
            stt = 'Waitting'
        elif tsk.taskState == TaskState.Started:
            stt = 'Started'
        elif tsk.taskState == TaskState.Done:
            stt = 'Done'
        elif tsk.taskState == TaskState.Assigned:
            stt = 'Assigned'
        strng = 'TaskId: '+ str(tsk.taskId) + '  |  Priority: ' +str(tsk.priority) + '  |  State: '+ stt + '  |  RobotId: '+ str(tsk.robotId)
        return strng
    
    def updateState(self, taskState):  # set the current task state
        self.taskState = taskState



def main(args=None):
    pose = [{0.0, 0.0, 0.25}, {0.0, 0.0, 0.0}]
    task = Task(1, 1, 1, pose, 1)
    task.robotId = 1
    task.updateState(TaskState.Waitting)
    print(task.taskToString(task))


if __name__ == '__main__':
    main()

