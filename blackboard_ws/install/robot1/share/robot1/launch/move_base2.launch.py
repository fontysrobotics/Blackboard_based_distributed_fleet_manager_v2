import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='odom_frame_id',
            default_value='robot2_tf/odom'
        ),
        launch.actions.DeclareLaunchArgument(
            name='base_frame_id',
            default_value='robot2_tf/base_footprint'
        ),
        launch.actions.DeclareLaunchArgument(
            name='global_frame_id',
            default_value='map'
        ),
        launch.actions.DeclareLaunchArgument(
            name='odom_topic',
            default_value='/robot2/odom'
        ),
        launch.actions.DeclareLaunchArgument(
            name='laser_topic',
            default_value='/robot2/laser/scan'
        ),
        launch.actions.DeclareLaunchArgument(
            name='move_forward_only',
            default_value='false'
        ),
        launch_ros.actions.Node(
            package='nav2_bt_navigator',
            executable='bt_navigator',
            name='move_base2',
            output='screen',
            parameters=[
                get_package_share_directory(
                    'robot1') + '/launch/move_base2.launch'
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
