import launch
import launch_ros.actions


def generate_launch_description():

    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='ros2_bbinstance',
            executable='blackboardinstance',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='ros2_bbinstance',
            executable='gui',
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
            executable='robotInstance2',
            name='robot2',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='ros2_bbinstance',
            executable='robotInstance3',
            name='robot3',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='ros2_bbinstance',
            executable='robotInstance4',
            name='robot4',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='ros2_bbinstance',
            executable='taskview',
            output='screen'                                 
        ),

               
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
