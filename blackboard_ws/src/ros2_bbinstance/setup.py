from setuptools import setup
import os
from glob import glob

package_name = 'ros2_bbinstance'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mpcmeulensteen',
    maintainer_email='mpcmeulensteen@hotmail.nl',
    description='TODO: Package description',
    license='BDS',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'blackboardinstance = ros2_bbinstance.blackboardinstance:main',
	    'gui = ros2_bbinstance.gui:main',
	    'robotInstance = ros2_bbinstance.robotInstance:main',
	    'taskview = ros2_bbinstance.taskview:main',
        ],
    },
)
