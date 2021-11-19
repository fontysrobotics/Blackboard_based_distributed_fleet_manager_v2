import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='set_base_frame',
            default_value='base_footprint'
        ),
        launch.actions.DeclareLaunchArgument(
            name='set_odom_frame',
            default_value='odom'
        ),
        launch.actions.DeclareLaunchArgument(
            name='set_map_frame',
            default_value='map'
        ),
        launch_ros.actions.Node(
            package='gmapping',
            executable='slam_gmapping',
            name='robot_slam_gmapping',
            output='screen',
            parameters=[
                {
                    'base_frame': launch.substitutions.LaunchConfiguration('set_base_frame')
                },
                {
                    'odom_frame': launch.substitutions.LaunchConfiguration('set_odom_frame')
                },
                {
                    'map_frame': launch.substitutions.LaunchConfiguration('set_map_frame')
                },
                {
                    'map_update_interval': '0.01'
                },
                {
                    'maxUrange': '10'
                },
                {
                    'sigma': '0.05'
                },
                {
                    'kernelSize': '1'
                },
                {
                    'lstep': '0.05'
                },
                {
                    'astep': '0.05'
                },
                {
                    'iterations': '5'
                },
                {
                    'lsigma': '0.075'
                },
                {
                    'ogain': '3.0'
                },
                {
                    'lskip': '0'
                },
                {
                    'minimumScore': '50'
                },
                {
                    'srr': '0.1'
                },
                {
                    'srt': '0.2'
                },
                {
                    'str': '0.1'
                },
                {
                    'stt': '0.2'
                },
                {
                    'linearUpdate': '1.0'
                },
                {
                    'angularUpdate': '0.2'
                },
                {
                    'temporalUpdate': '0.5'
                },
                {
                    'resampleThreshold': '0.5'
                },
                {
                    'particles': '100'
                },
                {
                    'xmin': '-10.0'
                },
                {
                    'ymin': '-10.0'
                },
                {
                    'xmax': '10.0'
                },
                {
                    'ymax': '10.0'
                },
                {
                    'delta': '0.05'
                },
                {
                    'llsamplerange': '0.01'
                },
                {
                    'llsamplestep': '0.01'
                },
                {
                    'lasamplerange': '0.005'
                },
                {
                    'lasamplestep': '0.005'
                }
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
