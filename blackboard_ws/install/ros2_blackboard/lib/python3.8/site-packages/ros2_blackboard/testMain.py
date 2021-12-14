import rclpy
from rclpy.node import Node
from message_pkg.msg import *
from std_msgs.msg import String
from ros2_blackboard.RosCommunication import Publisher
from ros2_blackboard.Battery import Battery
from ros2_blackboard.Robot import Robot
from ros2_blackboard.Blackboard import Blackboard

def main(args=None):
	##############################################################
	#testing blackboard.py and RosComunicate.py

	rclpy.init(args=args)
	publisher = Publisher('pubBlackboard')
	bb = Blackboard(1,publisher)
	#rclpy.spin_once(bb)
	

	##############################################################
	#testing Robot.py and Controller.py

	bat = Battery(100,1000,100)
	talker = Publisher('pubRobot')
	r = Robot('blackboard','robot1',1,1,1,1,5,10,10,bat,'robot1',talker, bb)  
	#rclpy.spin_once(r)
	
	rclpy.spin_once(r)

if __name__ == "__main__":
    main()
	