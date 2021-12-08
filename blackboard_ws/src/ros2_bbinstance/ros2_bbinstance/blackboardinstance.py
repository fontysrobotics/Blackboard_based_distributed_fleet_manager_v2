#!/usr/bin python3
import rclpy
from rclpy import publisher
from rclpy.node import Node
from ros2_blackboard import Publisher
from ros2_blackboard import Blackboard

def main(args=Node):
    rclpy.init(args=args)
    publisher = Publisher('blackboard')
    bb = Blackboard(1, publisher)
    rclpy.spin()

if __name__ == '__main__':
    main()