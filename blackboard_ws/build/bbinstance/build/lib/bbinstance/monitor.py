#!/usr/bin/env python

###############################################################################################
from python_qt_binding import QtWidgets
from python_qt_binding import QtCore
from python_qt_binding import QtGui
# from PyQt5 import QtCore, QtGui, QtWidgets

import rclpy
from message_pkg.msg import TaskMsg
from blackboard.Task import Task,TaskType,TaskStep,TaskState
from std_msgs.msg import String
from std_msgs.msg import Float32
from message_pkg.msg import BBbackup
from geometry_msgs.msg import Pose

from threading import Lock
import cv2




class Cbot(Node):
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (0,0,255)
        return cv2.circle(img,(self.x,self.y),self.radius,self.color,(-1))


if __name__ == "__main__":
    robot = Cbot(250,250,50)
