import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='use_map_topic',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='scan_topic',
            default_value='/robot4/scan'
        ),
        launch.actions.DeclareLaunchArgument(
            name='initial_pose_x',
            default_value='3.0'
        ),
        launch.actions.DeclareLaunchArgument(
            name='initial_pose_y',
            default_value='0.0'
        ),
        launch.actions.DeclareLaunchArgument(
            name='initial_pose_a',
            default_value='0.0'
        ),
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
        launch_ros.actions.Node(
            package='nav2_amcl',
            executable='amcl',
            name='amcl4',
            parameters=[
                {
                    'use_map_topic': launch.substitutions.LaunchConfiguration('use_map_topic')
                },
                {
                    'odom_model_type': 'diff'
                },
                {
                    'odom_alpha5': '0.1'
                },
                {
                    'gui_publish_rate': '10.0'
                },
                {
                    'laser_max_beams': '60'
                },
                {
                    'laser_max_range': '12.0'
                },
                {
                    'min_particles': '500'
                },
                {
                    'max_particles': '2000'
                },
                {
                    'kld_err': '0.05'
                },
                {
                    'kld_z': '0.99'
                },
                {
                    'odom_alpha1': '0.2'
                },
                {
                    'odom_alpha2': '0.2'
                },
                {
                    'odom_alpha3': '0.2'
                },
                {
                    'odom_alpha4': '0.2'
                },
                {
                    'laser_z_hit': '0.5'
                },
                {
                    'laser_z_short': '0.05'
                },
                {
                    'laser_z_max': '0.05'
                },
                {
                    'laser_z_rand': '0.5'
                },
                {
                    'laser_sigma_hit': '0.2'
                },
                {
                    'laser_lambda_short': '0.1'
                },
                {
                    'laser_model_type': 'likelihood_field'
                },
                {
                    'laser_likelihood_max_dist': '2.0'
                },
                {
                    'update_min_d': '0.25'
                },
                {
                    'update_min_a': '0.2'
                },
                {
                    'odom_frame_id': launch.substitutions.LaunchConfiguration('odom_frame_id')
                },
                {
                    'base_frame_id': launch.substitutions.LaunchConfiguration('base_frame_id')
                },
                {
                    'global_frame_id': launch.substitutions.LaunchConfiguration('global_frame_id')
                },
                {
                    'resample_interval': '1'
                },
                {
                    'transform_tolerance': '1.0'
                },
                {
                    'recovery_alpha_slow': '0.0'
                },
                {
                    'recovery_alpha_fast': '0.0'
                },
                {
                    'initial_pose_x': launch.substitutions.LaunchConfiguration('initial_pose_x')
                },
                {
                    'initial_pose_y': launch.substitutions.LaunchConfiguration('initial_pose_y')
                },
                {
                    'initial_pose_a': launch.substitutions.LaunchConfiguration('initial_pose_a')
                }
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
