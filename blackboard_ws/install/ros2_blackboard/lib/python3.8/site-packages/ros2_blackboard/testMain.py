import rclpy
from rclpy.node import Node
from message_pkg.msg import TaskMsg
from std_msgs.msg import String
from ros2_blackboard.RosCommunication import Publisher
from ros2_blackboard.Battery import Battery
from ros2_blackboard.Robot import Robot

from ros2_blackboard.Blackboard import Blackboard

def main(args=None):
	##############################################################
	#testing blackboard.py and RosComunicate.py

	rclpy.init(args=args)
	publisher = Publisher('bbinstance')
	bb = Blackboard(1,publisher)
	#rclpy.spin(bb)

	##############################################################
	#testing Robot.py and Controller.py

	#rclpy.init(args=args)
	#node = Node('robotInstance')
	bat = Battery(100,1000,100)
	talker = Publisher('robot1')
	r = Robot('blackboard','robot1',1,1,1,1,5,10,10,bat,'robot1',talker)  
	#rclpy.spin(r)

if __name__ == "__main__":
    main()