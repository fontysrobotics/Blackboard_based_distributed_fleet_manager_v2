#!/usr/bin/env python3
#
# Copyright 2019 ROBOTIS CO., LTD.
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
# Authors: Darby Lim
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
  

def generate_launch_description():

    #TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    urdf_file_name = 'turtlebot3_burger.urdf'
    #urdf_file_name = 'robot_description_urdf.urdf'
    sdf_file_name = 'model.sdf'
    
    
    sdf_model = os.path.join(
    	get_package_share_directory('turtlebot3_gazebo'),
    	'models/turtlebot3_burger',
    	sdf_file_name)
    
    #sdf_model = os.path.join(
   #	get_package_share_directory('robot1'),
   #	'models',
    #	sdf_file_name)
    	

    print('urdf_file_name : {}'.format(urdf_file_name))

       #urdf_path = os.path.join(
    #    get_package_share_directory('robot1'),
    #    'urdf',
    #    urdf_file_name)

    urdf_path = os.path.join(
        get_package_share_directory('turtlebot3_description'),
        'urdf',
        urdf_file_name
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=[urdf_path]),
        
        Node(
            package='gazebo_ros', 
            executable='spawn_entity.py', 
            arguments=['-entity', 'robot1', 
               '-file', sdf_model,
                  '-x', '0.0',
                  '-y', '0.0',
                  '-z', '0.0',
                  '-Y', '0.0'],
                  output='screen'),
        
        #Node(
        #    package='gazebo_ros', 
        #    executable='spawn_entity.py', 
        #    arguments=['-entity', 'robot2', 
        #       '-file', sdf_model,
        #          '-x', '1.0',
        #          '-y', '0.0',
        #          '-z', '0.0',
        #          '-Y', '0.0'],
        #          output='screen'),
    ])
    
    
    
