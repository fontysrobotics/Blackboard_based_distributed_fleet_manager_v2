#!/usr/bin python3
import rclpy
from ros2_blackboard.RosCommunication import NodePublisher
from ros2_blackboard.Blackboard import Blackboard

def main(args=None):
    rclpy.init(args=args)
    publisher = NodePublisher('blackboard_pub')
    bb = Blackboard(1, publisher)
    rclpy.spin(bb)

if __name__ == '__main__':
    main()