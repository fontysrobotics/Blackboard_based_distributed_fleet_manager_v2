#!/usr/bin python3
#need to point to classes inorder to import
import rclpy

from rclpy.node import Node
from blackboard.Robot import Robot
from blackboard.RosCommunication import Talker
from blackboard.Blackboard import Blackboard
from blackboard.Battery import Battery


def main(args=None):
	rclpy.init(args=args)
	node = Node('robotInstance4')
	bat = Battery(100,500,100)
	talker = Talker('robot4')
	r = Robot('blackboard','robot1',4,4,4,4,5,10,10,bat,'robot4',talker)
	rclpy.spin()

if __name__ == '__main__':
    main()
