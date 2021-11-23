Pkgs:
- navigation: Starts gazebo with environment and 2 robots by launching environment.launch.py
First i used this package to spawn turtlebot_burger in the 3d environment and navigate it with RVIZ. This worked so now i am trying to navigate without using turtlebot and using the robot_description_urdf.urdf but that doesnt work yet.

At the moment i spawn the 2 robots in robot_state_publisher.launch.py by executing spawn_entity.py (from the ros_gazebo package) 2 times. I dont think this is the right way to do it but i couldn't get it to work any other way. 

- navigate_robot_pkg: Launches Rviz and Nav2 to navigate the robot

- bbinstance: Should start the blackboard instance, robot instances and launch the gui (copied from the old prototype)
This is where i have my problem. First I had trouble building the python files as executables. Now when i try to launch blackboard.launch.py i get a permission error on all of the src files. 

- robot1: launches amcl and movebase for the robots

- blackboard: have not looked at this package yet. 


My problems:
Navigating the robot from the robot_description_urdf.urdf does not work yet. When i launch navigation2.launch.py in the navigate_robot_pkg i receive the error in RVIZ: "Frame [map] does not exist." When i try to 2D Pose Estimate it doesn't do anything. 

In bbinstance i copied the old python code. First i had trouble building the package with the python files as executables and now when i try to launch blackboard.launch.py i get a lot of errors. 
