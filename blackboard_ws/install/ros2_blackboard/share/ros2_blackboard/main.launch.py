from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    ld = LaunchDescription()
    launchNode = Node(
    package='ros2_blackboard',
    executable='testMain',
    name='testMain',
    prefix=['gdb -ex run --args'],
    output='screen')
    ld.add_action(launchNode)

    return ld