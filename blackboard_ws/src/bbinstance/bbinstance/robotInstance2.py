#!/usr/bin python3
#need to point to classes inorder to import
import rclpy

from rclpy.Node import Node
from blackboard.Robot import Robot
from blackboard.RosCommunication import Talker
from rosnode import rosnode_ping
from blackboard.Blackboard import Blackboard
from blackboard.Battery import Battery


def main(args=None):
	rclpy.init(args=args)
	node = Node('robotInstance2')
	bat = Battery(100,500,100)
	talker = Talker('robot2')
	r = Robot('blackboard','robot1',2,2,2,2,5,10,10,bat,'robot2',talker)
	rclpy.spin()

if __name__ == '__main__':
    main()
