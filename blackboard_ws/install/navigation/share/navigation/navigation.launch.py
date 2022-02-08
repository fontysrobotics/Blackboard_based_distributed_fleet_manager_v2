# Copyright 2019 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Darby Lim

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node



robot_launch_file_dir = os.path.join(get_package_share_directory('robot1'), 'launch')
nav2_launch_file_dir = os.path.join(get_package_share_directory('nav2_bringup'), 'launch')
rviz_config_dir = os.path.join(get_package_share_directory('navigation'), 'rviz', 'rviz_trobots.rviz')


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    map_dir = LaunchConfiguration('map',
        default=os.path.join(
            get_package_share_directory('navigation'),
            'maps',
            'env.yaml'))

    param_file_name = 'burger.yaml'
    param_dir = LaunchConfiguration(
        'params_file',
        default=os.path.join(
            get_package_share_directory('navigation'),
            'param',
            param_file_name))


    

    return LaunchDescription([
        DeclareLaunchArgument(
            'map',
            default_value=map_dir,
            description='Full path to map file to load'),

        DeclareLaunchArgument(
            'params_file',
            default_value=param_dir,
            description='Full path to param file to load'),

        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([nav2_launch_file_dir, '/bringup_launch.py']),
            launch_arguments={
                'map': map_dir,
                'use_sim_time': use_sim_time,
                'params_file': param_dir}.items(),
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_dir],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen'),
        
        Node(
            package='nav2_map_server',
            executable='map_saver_server.launch.py',
            name="map_server",
            arguments=[map_dir],
            parameters=[{"frame_id": "map"}]
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='link1_broadcaster1',
            arguments=["-3" "0" "0" "0" "0" "0" "1" "map" "robot1/base_footprint" "100"],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='link1_broadcaster2',
            arguments=["-1" "0" "0" "0" "0" "0" "1" "map" "robot1/base_footprint" "100"],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='link1_broadcaster3',
            arguments=["1" "0" "0" "0" "0" "0" "1" "map" "robot1/base_footprint" "100"],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='link1_broadcaster4',
            arguments=["3" "0" "0" "0" "0" "0" "1" "map" "robot1/base_footprint" "100"],
        ),
        IncludeLaunchDescription(
		    PythonLaunchDescriptionSource([robot_launch_file_dir, '/robot.launch.py']),
		    launch_arguments={'use_sim_time': use_sim_time}.items(),
		)
    ])
