from setuptools import setup

package_name = 'ros2_blackboard'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mpcmeulensteen',
    maintainer_email='mpcmeulensteen@hotmail.nl',
    description='Blackboard',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'RosCommunication = ros2_blackboard.RosCommunication:main',
            'testMain = ros2_blackboard.testMain:main',
        ],
    },
)
