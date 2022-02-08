#!/usr/bin python3
#need to point to classes inorder to import
import rclpy
from rclpy.node import Node

import ros2_blackboard
from ros2_blackboard.Robot import Robot
from ros2_blackboard.RosCommunication import NodePublisher
from ros2_blackboard.Blackboard import Blackboard
from ros2_blackboard.Battery import Battery


def main(args=None):
	rclpy.init(args=args)
	bat = Battery(100,1000,100)
	talker = NodePublisher('robot3_pub')
	r = Robot('blackboard','robot1',3,3,3,3,5,10,10,bat,'robot3',talker)  
	#rclpy.spin()

if __name__ == '__main__':
    main()