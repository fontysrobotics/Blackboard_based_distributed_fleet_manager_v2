import rclpy
from rclpy.node import Node
from std_msgs.msg import String              # Custom built ROS messages
from message_pkg.msg import TaskMsg          #
from message_pkg.msg import BBbackup         #
from message_pkg.msg import TaskCost         #
from message_pkg.msg import BBsynch          #
from message_pkg.msg import TaskStateMsg     #

class Publisher():
    def __init__(self, node):
        super().__init__(node.nodeName)
        
        self.publish_newTask = Node(node).create_publisher(self, TaskMsg, '/newTask', 1)         # new task publisher
        self.pub_robotState = Node(node).create_publisher(self, String,'/robotState',1)            # robot state to simulate defect
        self.pub_bbSync = Node(node).create_publisher(self, BBsynch,'/bbSync',1)                   # syncronize blackboard task list
        self.pub_taskBC = Node(node).create_publisher(self, TaskMsg,'/taskBC',1)                   # broadcast a task over topic
        self.pub_bbBackup = Node(node).create_publisher(self, BBbackup,'/bbBackup',1)              # blackboard and backup adresses
        self.pub_taskAssign = Node(node).create_publisher(self, TaskMsg,'/taskAssign',1)           # assign a task to robot
        self.pub_taskCost = Node(node).create_publisher(self, TaskCost,'/taskCost',1)              # send task cost from robots
        self.pub_taskState = Node(node).create_publisher(self, TaskStateMsg, '/TaskStateMsg',1)    # update task state in blackboare
    
    #def test():
      
      
        



#---------------------------------------------------------
#REMOVE - testing purposes
#def main(args=None):
 # rclpy.init(args=args)
 # publisher = Publisher("robot1")
  #sub = publisher.create_subscription(TaskMsg, '/newTask', publisher.test, 1)
  #rclpy.spin(publisher)

#if __name__ == '__main__':
 # main()
