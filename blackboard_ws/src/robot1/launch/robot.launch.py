import os
import sys

import launch
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    urdf_file_name = 'turtlebot3_burger.urdf'
    sdf_file_name = 'turtlebot3_burger/model.sdf'
    print("urdf_file_name : {}".format(urdf_file_name))

    urdf = os.path.join(get_package_share_directory('robot1'), 'urdf', urdf_file_name)

    sdf_model = os.path.join(get_package_share_directory('robot1'), 'models', sdf_file_name)

    with open(urdf, 'r') as infp:
        robot_desc = infp.read()


    ld = launch.LaunchDescription([
        
        Node(
          package='robot_state_publisher',
          executable='robot_state_publisher',
          name='robot_state_publisher1',
          output='screen',
          namespace='robot1',
          parameters=[
            {'use_sim_time': use_sim_time},
            {'frame_prefix': 'robot1_tf'},
            {'robot_description': robot_desc}],
          arguments=[urdf]),

        Node(
            package='gazebo_ros', 
            executable='spawn_entity.py', 
            arguments=['-entity', 'robot1', 
               '-file', sdf_model,
                  '-x', '-3.0',
                  '-y', '0.0',
                  '-z', '0.0',
                  '-Y', '0.0'],
            output='screen',
            namespace='robot1'),

        Node(
          package='robot_state_publisher',
          executable='robot_state_publisher',
          name='robot_state_publisher2',
          output='screen',
          namespace='robot2',
          parameters=[
            {'use_sim_time': use_sim_time},
            {'frame_prefix': 'robot2_tf'},
            {'robot_description': robot_desc}],
          arguments=[urdf]),

        Node(
        package='gazebo_ros', 
        executable='spawn_entity.py', 
        arguments=['-entity', 'robot2', 
            '-file', sdf_model,
                '-x', '-1.0',
                '-y', '0.0',
                '-z', '0.0',
                '-Y', '0.0'],
        output='screen',
        namespace='robot2'),

        Node(
          package='robot_state_publisher',
          executable='robot_state_publisher',
          name='robot_state_publisher3',
          output='screen',
          namespace='robot3',
          parameters=[
            {'use_sim_time': use_sim_time},
            {'frame_prefix': 'robot3_tf'},
            {'robot_description': robot_desc}],
          arguments=[urdf]),
        
        Node(
            package='gazebo_ros', 
            executable='spawn_entity.py', 
            arguments=['-entity', 'robot3', 
               '-file', sdf_model,
                  '-x', '1.0',
                  '-y', '0.0',
                  '-z', '0.0',
                  '-Y', '0.0'],
            output='screen',
            namespace='robot3'),

        Node(
          package='robot_state_publisher',
          executable='robot_state_publisher',
          name='robot_state_publisher4',
          output='screen',
          namespace='robot4',
          parameters=[
            {'use_sim_time': use_sim_time},
            {'frame_prefix': 'robot4_tf'},
            {'robot_description': robot_desc}],
          arguments=[urdf]),

        Node(
            package='gazebo_ros', 
            executable='spawn_entity.py', 
            arguments=['-entity', 'robot4', 
               '-file', sdf_model,
                  '-x', '3.0',
                  '-y', '0.0',
                  '-z', '0.0',
                  '-Y', '0.0'],
            output='screen',
            namespace='robot4'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'robot1'), 'launch/amcl1.launch.py')
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'robot1'), 'launch/move_base1.launch.py')
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'robot1'), 'launch/amcl2.launch.py')
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'robot1'), 'launch/move_base2.launch.py')
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'robot1'), 'launch/amcl3.launch.py')
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'robot1'), 'launch/move_base3.launch.py')
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'robot1'), 'launch/amcl4.launch.py')
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'robot1'), 'launch/move_base4.launch.py')
            )
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
