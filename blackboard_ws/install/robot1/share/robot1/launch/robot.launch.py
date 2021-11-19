import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'robot1'), 'launch/amcl1.launch.py')
            )
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'robot1'), 'launch/move_base1.launch.py')
            )
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'robot1'), 'launch/amcl2.launch.py')
            )
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'robot1'), 'launch/move_base2.launch.py')
            )
        ),
        #launch.actions.IncludeLaunchDescription(
         #   launch.launch_description_sources.PythonLaunchDescriptionSource(
          #      os.path.join(get_package_share_directory(
           #         'robot1'), 'launch/amcl3.launch.py')
            #)
        #),
        #launch.actions.IncludeLaunchDescription(
         #   launch.launch_description_sources.PythonLaunchDescriptionSource(
          #      os.path.join(get_package_share_directory(
           #         'robot1'), 'launch/move_base3.launch.py')
            #)
        #),
        #launch.actions.IncludeLaunchDescription(
         #   launch.launch_description_sources.PythonLaunchDescriptionSource(
          #      os.path.join(get_package_share_directory(
           #         'robot1'), 'launch/amcl4.launch.py')
            #)
        #),
        #launch.actions.IncludeLaunchDescription(
         #   launch.launch_description_sources.PythonLaunchDescriptionSource(
          #      os.path.join(get_package_share_directory(
           #         'robot1'), 'launch/move_base4.launch.py')
            #)
        #)
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
