#!/usr/bin python3
#need to point to classes inorder to import
import rclpy
from rclpy.node import Node

import blackboard
from blackboard.Robot import Robot
from blackboard.RosCommunication import Talker
from blackboard.Blackboard import Blackboard
from blackboard.Battery import Battery


def main(args=None):
	rclpy.init(args=args)
	node = Node('robotInstance')
	bat = Battery(100,1000,100)
	talker = Talker('robot1')
	r = Robot('blackboard','robot1',1,1,1,1,5,10,10,bat,'robot1',talker)  
	rclpy.spin()

if __name__ == '__main__':
    main()
