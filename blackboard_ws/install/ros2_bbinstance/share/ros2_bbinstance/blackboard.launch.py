from ament_index_python.packages import get_package_share_directory
import launch
import os
from launch.actions import include_launch_description, DeclareLaunchArgument
from launch.actions.include_launch_description import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.substitutions.launch_configuration import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
import launch_ros.actions


def generate_launch_description():
    
    world_file_name = 'environment.world'
    world = os.path.join(get_package_share_directory('navigation'), 
                'worlds', world_file_name)
    launch_file_dir = os.path.join(get_package_share_directory('navigation'), 'launch')
    robot_launch_file_dir = os.path.join(get_package_share_directory('robot1'), 'launch')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    #default_rviz_config_path = os.path.join(get_package_share_directory('navigation'), 'rviz/nav_cartographer.rviz')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    #rviz_config_file = LaunchConfiguration('rviz_config_file')
    #use_rviz = LaunchConfiguration('use_rviz')


    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='ros2_bbinstance',
            executable='blackboardinstance',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='ros2_bbinstance',
            executable='robotInstance',
            output='screen'
        ),
        #DeclareLaunchArgument(
        #    name='rviz_config_file',
        #    default_value=default_rviz_config_path,
        #    description='Full path to the RVIZ config file to use'),
        #DeclareLaunchArgument(
        #    name='use_rviz',
        #    default_value='True',
        #    description='Whether to start RVIZ'),
        #launch_ros.actions.Node(
        #    package='ros2_bbinstance',
        #    executable='taskview',
        #    output='screen'
        #),
        launch_ros.actions.Node(
            package='ros2_bbinstance',
            executable='gui',
            output='screen'
        ),
        #launch_ros.actions.Node(
        #    package='rviz2',
        #    executable='rviz2',
        #    name='rviz2',
        #    output='screen',
        #    arguments=['-d', rviz_config_file],
        #    condition=IfCondition(use_rviz)
        #),
        IncludeLaunchDescription(
		    PythonLaunchDescriptionSource(
			os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
		    ),
		    launch_arguments={'world': world}.items(),
		),
		IncludeLaunchDescription(
		    PythonLaunchDescriptionSource(
			os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
		    ),
		),
		IncludeLaunchDescription(
		    PythonLaunchDescriptionSource([launch_file_dir, '/robot_state_publisher.launch.py']),
		    launch_arguments={'use_sim_time': use_sim_time}.items(),
		),
		IncludeLaunchDescription(
		    PythonLaunchDescriptionSource([robot_launch_file_dir, '/robot.launch.py']),
		    launch_arguments={'use_sim_time': use_sim_time}.items(),
		)
        

               
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
