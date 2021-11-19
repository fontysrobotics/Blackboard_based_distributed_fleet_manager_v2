import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='bbinstance',
            executable='blackboardinstance.py',
            name='blackboard',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='bbinstance',
            executable='gui.py',
            name='gui',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='bbinstance',
            executable='robotInstance.py',
            name='robot1',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='bbinstance',
            executable='robotInstance2.py',
            name='robot2',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='bbinstance',
            executable='robotInstance3.py',
            name='robot3',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='bbinstance',
            executable='robotInstance4.py',
            name='robot4',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='bbinstance',
            executable='taskview.py',
            name='taskview',
            output='screen'
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
