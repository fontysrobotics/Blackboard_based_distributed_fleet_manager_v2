import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='odom_frame_id',
            default_value='robot4_tf/odom'
        ),
        launch.actions.DeclareLaunchArgument(
            name='base_frame_id',
            default_value='robot4_tf/base_footprint'
        ),
        launch.actions.DeclareLaunchArgument(
            name='global_frame_id',
            default_value='map'
        ),
        launch.actions.DeclareLaunchArgument(
            name='odom_topic',
            default_value='/robot4/odom'
        ),
        launch.actions.DeclareLaunchArgument(
            name='laser_topic',
            default_value='/robot4/laser/scan'
        ),
        launch.actions.DeclareLaunchArgument(
            name='move_forward_only',
            default_value='false'
        ),
        launch_ros.actions.Node(
            package='move_base',
            executable='move_base',
            name='move_base4',
            output='screen',
            parameters=[
                {
                    'base_local_planner': 'dwa_local_planner/DWAPlannerROS'
                },
                {
                    'DWAPlannerROS/min_vel_x': '0.0'
                },
                {
                    'global_costmap/global_frame': launch.substitutions.LaunchConfiguration('global_frame_id')
                },
                {
                    'global_costmap/robot_base_frame': launch.substitutions.LaunchConfiguration('base_frame_id')
                },
                {
                    'local_costmap/global_frame': launch.substitutions.LaunchConfiguration('odom_frame_id')
                },
                {
                    'local_costmap/robot_base_frame': launch.substitutions.LaunchConfiguration('base_frame_id')
                },
                {
                    'DWAPlannerROS/global_frame_id': launch.substitutions.LaunchConfiguration('odom_frame_id')
                },
                get_package_share_directory(
                    'robot1') + '/param/local_costmap_params.yaml',
                get_package_share_directory(
                    'robot1') + '/param/global_costmap_params.yaml',
                get_package_share_directory(
                    'robot1') + '/param/dwa_local_planner_params.yaml',
                get_package_share_directory(
                    'robot1') + '/param/move_base_params.yaml'
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
