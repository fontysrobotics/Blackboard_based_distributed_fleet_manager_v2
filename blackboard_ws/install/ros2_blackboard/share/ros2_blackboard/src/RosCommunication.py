import rclpy
from rclpy.node import Node
from std_msgs.msg import String              # Custom built ROS messages
from message_pkg.msg import TaskMsg          #
from message_pkg.msg import BBbackup         #
from message_pkg.msg import TaskCost         #
from message_pkg.msg import BBsynch          #
from message_pkg.msg import TaskStateMsg     #

class Publisher(Node):
    def __init__(self, nodeName):
        self.nodeName = nodeName
        super().__init__(self.nodeName)

        self.publish_newTask = Node.create_publisher(self, TaskMsg, '/newTask', 1)          # new task publisher
        self.pub_robotState = Node.create_publisher(self, String,'/robotState',1)            # robot state to simulate defect
        self.pub_bbSync = Node.create_publisher(self, BBsynch,'/BbSync',1)                   # syncronize blackboard task list
        self.pub_taskBC = Node.create_publisher(self, TaskMsg,'/taskBC',1)                   # broadcast a task over topic
        self.pub_bbBackup = Node.create_publisher(self, BBbackup,'/bbBackup',1)              # blackboard and backup adresses
        self.pub_taskAssign = Node.create_publisher(self, TaskMsg,'/taskAssign',1)           # assign a task to robot
        self.pub_taskCost = Node.create_publisher(self, TaskCost,'/taskCost',1)              # send task cost from robots
        self.pub_taskState = Node.create_publisher(self, TaskStateMsg, '/TaskStateMsg',1)    # update task state in blackboare
        node = rclpy.create_node(nodeName)

def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher("robot1")

    rclpy.spin(publisher)

if __name__ == '__main__':
    main()