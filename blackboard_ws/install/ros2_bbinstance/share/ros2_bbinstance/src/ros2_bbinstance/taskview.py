#!/usr/bin python3

from python_qt_binding import QtWidgets, QtCore
import sys
import rclpy 
from message_pkg.msg import BBsync
from rclpy.node import Node
from ros2_blackboard.Task import Task, TaskState
from threading import Lock
from ros2_bbinstance.rviz_tools import RvizMarkers
from ros2_blackboard.RosCommunication import NodePublisher


class Ui_MainWindow(Node, object):
    def __init__(self):
        super().__init__('taskview')   
        #self.create_timer(2, self.viewTasks)

        

    def setupUi(self, MainWindow):
        self.lock = Lock()
        publisher = NodePublisher('taskview_pub')
        self.pubNewTask = publisher.pub_bbSync
        self.create_subscription(BBsync, 'bbSync', self.taskview, 1)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 40, 771, 521))
        self.listView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tasklist = []
        self.markers = RvizMarkers('/map','/markers')
       

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Task View"))
        self.label.setText(_translate("MainWindow", "Tasks"))

    def taskview(self, data):
        self.tasklist = []
        print(data)
        for taskmsg in data.tasks:
            task = Task(taskmsg.taskid, taskmsg.priority, taskmsg.tasktype, taskmsg.pose, taskmsg.payload)
            task.robotid = taskmsg.robotid
            task.cost = taskmsg.cost
            task.taskstate = taskmsg.taskstate
            self.tasklist.append(task)
        self.createMarkers()
        self.viewTasks()

    def viewTasks(self):
        self.listView.clear()
        for t in self.tasklist:
            tmpstr = self.taskToString(t)
            self.listView.addItem(tmpstr)
    
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
    
    def createMarkers(self):
        self.markers.deleteAllMarkers()
        stepCounter = 0

        for t in self.tasklist:
            if t.taskstate != 2:
                finalStep = 0
                length = len(t.pose)
                for po in t.pose:
                    finalStep = finalStep + 1
                    markerpose = po
                    markerpose.orientation.x = 1.0
                    markerpose.orientation.y = 0.0
                    markerpose.orientation.z = -1.0
                    markerpose.orientation.w = 0.0
                    markerpose.position.z = 0.5
                    scale = 0.5
                    id = t.taskId+stepCounter
                    color = 'gray'
                    if t.robotId == 1:
                        color = 'green'
                    if t.robotId == 2:
                        color = 'red'
                    if t.robotId == 3:
                        color = 'orange'
                    if t.robotId == 4:
                        color = 'yellow'
                    if finalStep == length:
                        markerpose.position.z = 1.0
                        scale = 1.0
                    self.markers.publishArrow(markerpose,color,scale,lifetime=100)
                    stepCounter = stepCounter+1
        

def main(args=None):
    rclpy.init(args=args)
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    rclpy.spin_once(ui)
    sys.exit(app.exec_())
    
    
if __name__ == "__main__":
    main()
    
    

