import rclpy
from rclpy.node import Node
from std_msgs.msg import String              # Custom built ROS messages
from message_pkg.msg import TaskMsg          #
from message_pkg.msg import BBbackup         #
from message_pkg.msg import TaskCost         #
from message_pkg.msg import BBsynch          #
from message_pkg.msg import TaskStateMsg     #

class Talker(Node):
    def __init__(self, nodeName):
        self.nodeName = nodeName
        super().__init__(self.nodeName)

        self.publish_newTask = Node.create_publisher(TaskMsg, '/newTask', 1)
        node = rclpy.create_node(nodeName)