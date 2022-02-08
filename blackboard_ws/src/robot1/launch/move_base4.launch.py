
import launch
import launch_ros.actions
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from pathlib import Path

costmap_common_params_filepath = Path(get_package_share_directory('robot1'), 'param', 'costmap_common_params.yaml')
local_costmap_params_filepath = Path(get_package_share_directory('robot1'), 'param', 'local_costmap_params.yaml') 
global_costmap_params_filepath = Path(get_package_share_directory('robot1'), 'param', 'global_costmap_params.yaml')
dwb_local_planner_params_filepath = Path(get_package_share_directory('robot1'), 'param', 'dwb_local_planner_params.yaml')
move_base_params_filepath = Path(get_package_share_directory('robot1'), 'param', 'move_base_params.yaml')

odom_frame_id_arg = DeclareLaunchArgument(
        "odom_frame_id", default_value="robot4_tf/odom"
    )
base_frame_id_arg = DeclareLaunchArgument(
    "base_frame_id", default_value="robot4_tf/base_footprint"
)
global_frame_id_arg = DeclareLaunchArgument(
    "global_frame_id", default_value="map"
)
odom_topic_arg = DeclareLaunchArgument(
    "odom_topic", default_value="/robot4/odom"
)
laser_topic_arg = DeclareLaunchArgument(
    "laser_topic", default_value="/robot4/laser/scan"
)
move_forward_only_arg = DeclareLaunchArgument(
    "move_forward_only", default_value="false"
)


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='odom_frame_id',
            default_value='robot4_tf/odom'
        ),
        launch.actions.DeclareLaunchArgument(
            name='base_frame_id',
            default_value='robot4_tf/base_footprint'
        ),
        launch.actions.DeclareLaunchArgument(
            name='global_frame_id',
            default_value='map'
        ),
        launch.actions.DeclareLaunchArgument(
            name='odom_topic',
            default_value='/robot4/odom'
        ),
        launch.actions.DeclareLaunchArgument(
            name='laser_topic',
            default_value='/robot4/laser/scan'
        ),
        launch.actions.DeclareLaunchArgument(
            name='move_forward_only',
            default_value='false'
        ),
        launch_ros.actions.Node(
            package='nav2_bt_navigator',
            executable='bt_navigator',
            name='move_base4',
            output='screen',
            respawn='false',
            parameters=[
                {"base_local_planner": "dwb_local_planner/dwb_core"},
                costmap_common_params_filepath, 
                local_costmap_params_filepath,
                global_costmap_params_filepath,
                dwb_local_planner_params_filepath,
                move_base_params_filepath,
                {"DWBPlannerROS/min_vel_x": "0.0"},
                {"global_costmap/global_frame": 'global_frame_id'},
                {"global_costmap/robot_base_frame": 'base_frame_id'},
                {"local_costmap/global_frame": 'odom_frame_id'},
                {"local_costmap/robot_base_frame": 'base_frame_id'},
                {"DWBPlannerROS/global_frame_id": 'odom_frame_id'}               
            ],
            remappings=[
                ('/cmd_vel'                                                         , '/robot4/cmd_vel'),
                ('/odom'                                                            , LaunchConfiguration('odom_topic')),
                ('/scan'                                                            , LaunchConfiguration('laser_topic')),
                ('map', '/map'),
                ('/move_base_simple/goal'                                           , '/robot4/move_base_simple/goal'),
                ('/move_base/TebLocalPlannerRos/global_plan'                        , '/robot4/move_base/TebLocalPlannerRos/global_plan'),
                ('/move_base/TebLocalPlannerRos/local_plan'                         , '/robot4/move_base/TebLocalPlannerRos/local_plan'),
                ('/move_base/TebLocalPlannerRos/teb_markers_array'                  , '/robot4/move_base/TebLocalPlannerRos/teb_markers_array'),
                ('/move_base/TebLocalPlannerRos/teb_markers'                        , '/robot4/move_base/TebLocalPlannerRos/teb_markers'),
                ('/move_base/TebLocalPlannerRos/teb_poses'                          , '/robot4/move_base/TebLocalPlannerRos/teb_poses'),
                ('/move_base/global_costmap/costmap'                                , '/robot4/move_base/global_costmap/costmap'),
                ('/move_base/global_costmap/costmap_updates'                        , '/robot4/move_base/global_costmap/costmap_updates'),
                ('/move_base/local_costmap/costmap'                                 , '/robot4/move_base/local_costmap/costmap'),
                ('/move_base/local_costmap/costmap_updates'                         , '/robot4/move_base/local_costmap/costmap_updates'),
                ('/move_base/local_costmap/footprint'                               , '/robot4/move_base/local_costmap/footprint'),

                ('/move_base/GlobalPlanner/parameter_descriptions'                  , '/robot4/move_base/GlobalPlanner/parameter_descriptions'),
                ('/move_base/GlobalPlanner/parameter_updates'                       , '/robot4/move_base/GlobalPlanner/parameter_updates'),
                ('/move_base/GlobalPlanner/plan'                                    , '/robot4/move_base/GlobalPlanner/plan'),
                ('/move_base/GlobalPlanner/potential'                               , '/robot4/move_base/GlobalPlanner/potential'),
                ('/move_base/TebLocalPlannerROS/obstacles'                          , '/robot4/move_base/TebLocalPlannerROS/obstacles'),
                ('/move_base/TebLocalPlannerROS/parameter_descriptions'             , '/robot4/move_base/TebLocalPlannerROS/parameter_descriptions'),
                ('/move_base/TebLocalPlannerROS/parameter_updates'                  , '/robot4/move_base/TebLocalPlannerROS/parameter_updates'),
                ('/move_base/cancel'                                                , '/robot4/move_base/cancel'),
                ('/move_base/current_goal'                                          , '/robot4/move_base/current_goal'),
                ('/move_base/feedback'                                              , '/robot4/move_base/feedback'),
                ('/move_base/global_costmap/footprint'                              , '/robot4/move_base/global_costmap/footprint'),
                ('/move_base/global_costmap/inflation_layer/parameter_descriptions' , '/robot4/move_base/global_costmap/inflation_layer/parameter_descriptions'),
                ('/move_base/global_costmap/inflation_layer/parameter_updates'      , '/robot4/move_base/global_costmap/inflation_layer/parameter_updates'),
                ('/move_base/global_costmap/obstacle_layer/clearing_endpoints'      , '/robot4/move_base/global_costmap/obstacle_layer/cleraing_endpoints'),
                ('/move_base/global_costmap/obstacle_layer/parameter_descriptions'  , '/robot4/move_base/global_costmap/obstacle_layers/parameter_descriptions'),
                ('/move_base/global_costmap/obstacle_layer/parameter_updates'       , '/robot4/move_base/global_costmap/obstacle_layers/parameter_updates'),
                ('/move_base/global_costmap/parameter_descriptions'                 , '/robot4/move_base/global_costmap/parameter_descriptions'),
                ('/move_base/global_costmap/parameter_updates'                      , '/robot4/move_base/global_costmap/parameter_updates'),
                ('/move_base/global_costmap/static_layer/parameter_descriptions'    , '/robot4/move_base/global_costmap/static_layer/parameter_descriptions'),
                ('/move_base/global_costmap/static_layer/parameter_updates'         , '/robot4/move_base/global_costmap/static_layer/parameter_updates'),
                ('/move_base/goal'                                                  , '/robot4/move_base/goal'),
                ('/move_base/local_costmap/obstacle_layer/parameter_descriptions'   , '/robot4/move_base/local_costmap/obstacle_layer/parameter_descriptions'),
                ('/move_base/local_costmap/obstacle_layer/parameter_updates'        , '/robot4/move_base/local_costmap/obstacle_layer/parameter_updates'),
                ('/move_base/local_costmap/parameter_descriptions'                  , '/robot4/move_base/local_costmap/parameter_descriptions'),
                ('/move_base/local_costmap/static_layer/parameter_descriptions'     , '/robot4/move_base/local_costmap/static_layer/parameter_descriptions'),
                ('/move_base/local_costmap/static_layer/parameter_updates'          , '/robot4/move_base/local_costmap/static_layer/parameter_updates'),
                ('/move_base/parameter_descriptions'                                , '/robot4/move_base/parameter_descriptions'),
                ('/move_base/parameter_updates'                                     , '/robot4/move_base/parameter_updates'),
                ('/move_base/result'                                                , '/robot4/move_base/result'),
                ('/move_base/status'                                                , '/robot4/move_base/status'),
            ]
        )

    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
