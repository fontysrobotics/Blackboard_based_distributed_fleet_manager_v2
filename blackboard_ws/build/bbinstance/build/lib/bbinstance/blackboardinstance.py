#!/usr/bin python3
#need to point to classes inorder to import
import rclpy
from rclpy.node import Node
from message_pkg.msg import TaskMsg
from std_msgs.msg import String
from ros2_blackboard.RosCommunication import Talker

from ros2_blackboard.Blackboard import Blackboard

def main(args=None):
	rclpy.init(args=args)
	node = Node('bbinstance')
	talker = Talker('blackboard')
	bb = Blackboard(1,talker)
	rclpy.spin()


if __name__ == '__main__':
    main()
