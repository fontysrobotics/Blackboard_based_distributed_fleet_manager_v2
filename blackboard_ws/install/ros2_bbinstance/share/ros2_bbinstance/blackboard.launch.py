import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='ros2_bbinstance',
            executable='blackboardinstance',
            name='blackboard',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='ros2_bbinstance',
            executable='gui',
            name='gui',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='ros2_bbinstance',
            executable='robotInstance',
            name='robot1',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='ros2_bbinstance',
            executable='taskview',
            name='taskview',
            output='screen'
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
