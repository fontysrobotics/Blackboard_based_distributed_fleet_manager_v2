import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='bbinstance',
            executable='blackboardinstance',
            name='blackboard',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='bbinstance',
            executable='gui',
            name='gui',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='bbinstance',
            executable='robotInstance',
            name='robot1',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='bbinstance',
            executable='robotInstance2',
            name='robot2',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='bbinstance',
            executable='robotInstance3',
            name='robot3',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='bbinstance',
            executable='robotInstance4',
            name='robot4',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='bbinstance',
            executable='taskview',
            name='taskview',
            output='screen'
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
