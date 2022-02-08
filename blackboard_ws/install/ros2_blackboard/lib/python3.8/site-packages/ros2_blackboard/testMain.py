import rclpy
from rclpy.node import Node
#from message_pkg.msg import BBbackup, BBsynch, TaskCost, TaskMsg, TaskStateMsg
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
	rclpy.spin(bb)
	

	##############################################################
	#testing Robot.py and Controller.py

	#bat = Battery(100,1000,100)
	#talker = Publisher('pubRobot')
	#r = Robot('blackboard','robot1',1,1,1,1,5,10,10,bat,'robot1',talker)  
	#rclpy.spin_once(r)
	
	#rclpy.spin_once(r)

if __name__ == "__main__":
    main()
	