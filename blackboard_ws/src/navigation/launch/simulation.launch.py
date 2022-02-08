import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription, condition
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

def generate_launch_description():
    robot_launch_file_dir = os.path.join(get_package_share_directory('robot1'), 'launch')
    rviz_config_dir = os.path.join(get_package_share_directory('navigation'), 'rviz', 'rviz_trobots.rviz')
    rviz_map_file_dir = os.path.join(get_package_share_directory('navigation'), 'maps', 'env.yaml')
    map_server_file_dir = os.path.join(get_package_share_directory('navigation'), 'maps', 'server_map.yaml')
    world_path = os.path.join(get_package_share_directory('navigation'), 'worlds', 'environment.world')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')


    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    map_dir = LaunchConfiguration('map', default=rviz_map_file_dir)
    map_server_param = LaunchConfiguration('map_server_param', default=map_server_file_dir)
    headless = LaunchConfiguration('headless')
    use_simulator = LaunchConfiguration('use_simulator')
    world = LaunchConfiguration('world')


    declare_simulator_cmd = DeclareLaunchArgument(
        name='headless',
        default_value='False',
        description='Whether to execute gzclient')


    declare_gui_cmd = DeclareLaunchArgument(
        name='gui',
        default_value='true'
    )

    declare_use_sim_time_cmd = DeclareLaunchArgument(
        name='use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true')
 
    declare_use_simulator_cmd = DeclareLaunchArgument(
        name='use_simulator',
        default_value='True',
        description='Whether to start the simulator')
 
    declare_world_cmd = DeclareLaunchArgument(
        name='world',
        default_value=world_path,
        description='Full path to the world model file to load')



    start_gazebo_server_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')),
        condition=IfCondition(use_simulator),
        launch_arguments={'world': world}.items())
 
  
    start_gazebo_client_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')),
        condition=IfCondition(PythonExpression([use_simulator, ' and not ', headless])))
    
    start_rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_dir],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen')

    start_server_map = Node(
        package='nav2_map_server',
        executable='map_server',
        name="map_server",
        parameters=[map_server_param],
        output = "screen"
    )

    start_tf1 = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='link1_broadcaster1',
        arguments=['-3','0', '0', '0', '0', '0', 'map', 'robot1/base_footprint'],
        output = "screen"
    )

    start_tf2 = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='link1_broadcaster2',
        arguments=['-1','0', '0', '0', '0', '0', 'map', 'robot1/base_footprint'],
    )

    start_tf3 = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='link1_broadcaster3',
        arguments=['1','0', '0', '0', '0', '0', 'map', 'robot1/base_footprint'],
    )

    start_tf4 = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='link1_broadcaster4',
        arguments=['3','0', '0', '0', '0', '0', 'map', 'robot1/base_footprint'],
    )


    start_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([robot_launch_file_dir, '/robot.launch.py']),
        launch_arguments={'use_sim_time': use_sim_time}.items())

    ld = LaunchDescription()

    ld.add_action(declare_simulator_cmd)
    ld.add_action(declare_use_sim_time_cmd)
    ld.add_action(declare_use_simulator_cmd)
    ld.add_action(declare_world_cmd)
    
    # Add any actions
    ld.add_action(start_gazebo_server_cmd)
    ld.add_action(start_gazebo_client_cmd)
    ld.add_action(start_rviz)
    ld.add_action(start_server_map)
    ld.add_action(start_tf1)
    ld.add_action(start_tf2)
    ld.add_action(start_tf3)
    ld.add_action(start_tf4)

    ld.add_action(start_robot)

    return ld
 
