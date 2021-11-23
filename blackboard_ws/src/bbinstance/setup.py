from setuptools import setup

package_name = 'bbinstance'

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
    description='TODO: Package description',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'blackboardinstance = bbinstance.blackboardinstance:main',
	    'gui = bbinstance.gui:main',
	    'robotInstance = bbinstance.robotInstance:main',
	    'robotInstance2 = bbinstance.robotInstance2:main',
	    'robotInstance3 = bbinstance.robotInstance3:main',
	    'robotInstance4 = bbinstance.robotInstance4:main',
	    'taskview = bbinstance.taskview:main',
        ],
    },
)
