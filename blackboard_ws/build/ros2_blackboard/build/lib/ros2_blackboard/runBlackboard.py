import rclpy
from rclpy.node import Node
from message_pkg.msg import TaskMsg
from std_msgs.msg import String
from ros2_blackboard.RosCommunication import NodePublisher
from ros2_blackboard.Battery import Battery
from ros2_blackboard.Robot import Robot

from ros2_blackboard.Blackboard import Blackboard

def main(args=None):
	##############################################################
	#testing blackboard.py and RosComunicate.py

	rclpy.init(args=args)
	publisher = NodePublisher('pubBlackboard')
	bb = Blackboard(1,publisher)
	#rclpy.spin(bb)

	##############################################################
	#testing Robot.py and Controller.py

	#rclpy.init(args=args)
	#node = Node('robotInstance')
	bat = Battery(100,1000,100)
	talker = NodePublisher('pubRobot')
	r = Robot('blackboard','robot1',1,1,1,1,5,10,10,bat,'robot1',talker, bb)  
	#rclpy.spin(r)

if __name__ == "__main__":
    main()