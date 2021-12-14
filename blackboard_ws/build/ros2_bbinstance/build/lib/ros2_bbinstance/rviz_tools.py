import numpy
import random

from numpy.lib.function_base import delete

import rclpy
from tf_transformations import quaternion_from_matrix
from rclpy.duration import Duration
from rclpy.node import Node
from rclpy.node import Publisher
from std_msgs.msg import Header, ColorRGBA
from geometry_msgs.msg import Transform, Pose, Point, Point32, Vector3, Quaternion, Polygon
from visualization_msgs.msg import Marker

class RvizMarkers(Node):
    def __init__(self, base_frame, marker_topic, wait_time=None):
        self.base_frame = base_frame
        self.marker_topic = marker_topic

        self.setDefaultMarkerParams()

        self.loadMarkerPublisher(wait_time)

    def setDefaultMarkerParams(self):
        self.marker_lifetime = Duration(0.0) # 0 = Marker never expires
        self.muted = False
        self.alpha = 1.0

        # Set default parameters for Cylinder Marker
        self.cylinder_marker = Marker()
        self.cylinder_marker.header.frame_id = self.base_frame
        self.cylinder_marker.ns = "Cylinder" # unique ID
        self.cylinder_marker.action = Marker().ADD
        self.cylinder_marker.type = Marker().CYLINDER
        self.cylinder_marker.lifetime = self.marker_lifetime

        # Reset Marker
        self.reset_marker = Marker()
        self.reset_marker.header.frame_id = self.base_frame
        self.reset_marker.header.stamp = self.get_clock()
        self.reset_marker.action = 3

        # Arrow Marker
        self.arrow_marker = Marker()
        self.arrow_marker.header.frame_id = self.base_frame
        self.arrow_marker.ns = "Arrow" # unique ID
        self.arrow_marker.action = Marker().ADD
        self.arrow_marker.type = Marker().ARROW
        self.arrow_marker.lifetime = self.marker_lifetime

        # Rectangle Marker
        self.rectangle_marker = Marker()
        self.rectangle_marker.header.frame_id = self.base_frame
        self.rectangle_marker.ns = "Rectangle" # unique ID
        self.rectangle_marker.action = Marker().ADD
        self.rectangle_marker.type = Marker().CUBE
        self.rectangle_marker.lifetime = self.marker_lifetime

        # Line Marker
        self.line_marker = Marker()
        self.line_marker.header.frame_id = self.base_frame
        self.line_marker.ns = "Line" # unique ID
        self.line_marker.action = Marker().ADD
        self.line_marker.type = Marker().LINE_STRIP
        self.line_marker.lifetime = self.marker_lifetime

        # Path Marker (Line List)
        self.path_marker = Marker()
        self.path_marker.header.frame_id = self.base_frame
        self.path_marker.ns = "Path" # unique ID
        self.path_marker.action = Marker().ADD
        self.path_marker.type = Marker().LINE_LIST
        self.path_marker.lifetime = self.marker_lifetime
        self.path_marker.pose.position.x = 0.0
        self.path_marker.pose.position.y = 0.0
        self.path_marker.pose.position.z = 0.0
        self.path_marker.pose.orientation.x = 0.0
        self.path_marker.pose.orientation.y = 0.0
        self.path_marker.pose.orientation.z = 0.0
        self.path_marker.pose.orientation.w = 1.0

        # Sphere Marker (A single sphere)
        # This renders a low-quality sphere
        self.sphere_marker = Marker()
        self.sphere_marker.header.frame_id = self.base_frame
        self.sphere_marker.ns = "Sphere" # unique ID
        self.sphere_marker.type = Marker().SPHERE
        self.sphere_marker.action = Marker().ADD
        self.sphere_marker.lifetime = self.marker_lifetime
        self.sphere_marker.pose.position.x = 0
        self.sphere_marker.pose.position.y = 0
        self.sphere_marker.pose.position.z = 0
        self.sphere_marker.pose.orientation.x = 0.0
        self.sphere_marker.pose.orientation.y = 0.0
        self.sphere_marker.pose.orientation.z = 0.0
        self.sphere_marker.pose.orientation.w = 1.0

        # Sphere Marker #2 (A single sphere)
        # A Sphere List with one sphere, this renders a
        # higher-quality sphere than the method above
        self.sphere_marker2 = Marker()
        self.sphere_marker2.header.frame_id = self.base_frame
        self.sphere_marker2.ns = "Sphere" # unique ID
        self.sphere_marker2.type = Marker().SPHERE_LIST
        self.sphere_marker2.action = Marker().ADD
        self.sphere_marker2.lifetime = self.marker_lifetime
        self.sphere_marker2.pose.position.x = 0
        self.sphere_marker2.pose.position.y = 0
        self.sphere_marker2.pose.position.z = 0
        self.sphere_marker2.pose.orientation.x = 0.0
        self.sphere_marker2.pose.orientation.y = 0.0
        self.sphere_marker2.pose.orientation.z = 0.0
        self.sphere_marker2.pose.orientation.w = 1.0
        point1 = Point()
        self.sphere_marker2.points.append(point1)
        self.sphere_marker2.colors.append(self.getColor('blue'))

        # Spheres List (Multiple spheres)
        self.spheres_marker = Marker()
        self.spheres_marker.header.frame_id = self.base_frame
        self.spheres_marker.ns = "Spheres" # unique ID
        self.spheres_marker.type = Marker().SPHERE_LIST
        self.spheres_marker.action = Marker().ADD
        self.spheres_marker.lifetime = self.marker_lifetime
        self.spheres_marker.pose.position.x = 0.0
        self.spheres_marker.pose.position.y = 0.0
        self.spheres_marker.pose.position.z = 0.0
        self.spheres_marker.pose.orientation.x = 0.0
        self.spheres_marker.pose.orientation.y = 0.0
        self.spheres_marker.pose.orientation.z = 0.0
        self.spheres_marker.pose.orientation.w = 1.0

        # Cube Marker (Block or cuboid)
        self.cube_marker = Marker()
        self.cube_marker.header.frame_id = self.base_frame
        self.cube_marker.ns = "Block" # unique ID
        self.cube_marker.action = Marker().ADD
        self.cube_marker.type = Marker().CUBE
        self.cube_marker.lifetime = self.marker_lifetime

        # Cubes List (Multiple cubes)
        self.cubes_marker = Marker()
        self.cubes_marker.header.frame_id = self.base_frame
        self.cubes_marker.ns = "Cubes" # unique ID
        self.cubes_marker.type = Marker().CUBE_LIST
        self.cubes_marker.action = Marker().ADD
        self.cubes_marker.lifetime = self.marker_lifetime
        self.cubes_marker.pose.position.x = 0.0
        self.cubes_marker.pose.position.y = 0.0
        self.cubes_marker.pose.position.z = 0.0
        self.cubes_marker.pose.orientation.x = 0.0
        self.cubes_marker.pose.orientation.y = 0.0
        self.cubes_marker.pose.orientation.z = 0.0
        self.cubes_marker.pose.orientation.w = 1.0

        # Cylinder Marker
        self.cylinder_marker = Marker()
        self.cylinder_marker.header.frame_id = self.base_frame
        self.cylinder_marker.ns = "Cylinder" # unique ID
        self.cylinder_marker.action = Marker().ADD
        self.cylinder_marker.type = Marker().CYLINDER
        self.cylinder_marker.lifetime = self.marker_lifetime

        # Mesh Marker
        self.mesh_marker = Marker()
        self.mesh_marker.header.frame_id = self.base_frame
        self.mesh_marker.ns = "Mesh" # unique ID
        self.mesh_marker.action = Marker().ADD
        self.mesh_marker.type = Marker().MESH_RESOURCE
        self.mesh_marker.lifetime = self.marker_lifetime

        # Text Marker
        self.text_marker = Marker()
        self.text_marker.header.frame_id = self.base_frame
        self.text_marker.ns = "Text" # unique ID
        self.text_marker.action = Marker().ADD
        self.text_marker.type = Marker().TEXT_VIEW_FACING
        self.text_marker.lifetime = self.marker_lifetime

    def loadMarkerPublisher(self, wait_time=None):
        if hasattr(self, 'pub_rviz_marker'):
            return

        self.pub_rviz_marker = self.create_publisher(Marker, self.marker_topic, 1)

        if wait_time != None:
            self.waitForSubscriber(self.pub_rviz_marker, wait_time)

    
    def waitForSubscriber(self, publisher, wait_time=1.0):
        start_time = self.get_clock().now()
        max_time = start_time + Duration(wait_time)

        num_existing_subscribers = Publisher(publisher).get_subscription_count()
        while (num_existing_subscribers == 0):
            rate = self.create_rate(100)
            rate.sleep()

            if (self.get_clock().now() > max_time):
                self.get_logger().info('No subscribers connected to the %s topic after %f seconds', self.marker_topic, wait_time)
                return False
            
            num_existing_subscribers = Publisher(publisher).get_subscription_count()
        return True
    
    def publishMarker(self, marker):

        if (self.muted == True):
            return True
        
        self.pub_rviz_marker.publish(marker)

        return True
    
    def deleteAllMarkers(self):
        return self.publishMarker(self.reset_marker)

    def getColor(self, color):

        result = ColorRGBA()
        result.a = self.alpha

        if (type(color) == tuple) or (type(color) == list):
            if len(color) == 3:
                result.r = color[0]
                result.g = color[1]
                result.b = color[2]
            elif len(color) == 4:
                result.r = color[0]
                result.g = color[1]
                result.b = color[2]
                result.a = color[3]
            else:
                raise ValueError('color must have 3 or 4 float values in getColor()')
        elif (color == 'red'):
            result.r = 0.8
            result.g = 0.1
            result.b = 0.1
        elif (color == 'green'):
            result.r = 0.1
            result.g = 0.8
            result.b = 0.1
        elif (color == 'blue'):
            result.r = 0.1
            result.g = 0.1
            result.b = 0.8
        elif (color == 'grey') or (color == 'gray'):
            result.r = 0.9
            result.g = 0.9
            result.b = 0.9
        elif (color == 'white'):
            result.r = 1.0
            result.g = 1.0
            result.b = 1.0
        elif (color == 'orange'):
            result.r = 1.0
            result.g = 0.5
            result.b = 0.0
        elif (color == 'translucent_light'):
            result.r = 0.1
            result.g = 0.1
            result.b = 0.1
            result.a = 0.1
        elif (color == 'translucent'):
            result.r = 0.1
            result.g = 0.1
            result.b = 0.1
            result.a = 0.25
        elif (color == 'translucent_dark'):
            result.r = 0.1
            result.g = 0.1
            result.b = 0.1
            result.a = 0.5
        elif (color == 'black'):
            result.r = 0.0
            result.g = 0.0
            result.b = 0.0
        elif (color == 'yellow'):
            result.r = 1.0
            result.g = 1.0
            result.b = 0.0
        elif (color == 'brown'):
            result.r = 0.597
            result.g = 0.296
            result.b = 0.0
        elif (color == 'pink'):
            result.r = 1.0
            result.g = 0.4
            result.b = 1
        elif (color == 'lime_green'):
            result.r = 0.6
            result.g = 1.0
            result.b = 0.2
        elif (color == 'clear'):
            result.r=1.0
            result.g=1.0
            result.b=1.0
            result.a=0.0
        elif (color == 'purple'):
            result.r = 0.597
            result.g = 0.0
            result.b = 0.597
        elif(color == 'random'):
            while True:
                result.r = random.random()
                result.b = random.random()
                result.g = random.random()
                if ((result.r + result.g + result.b) > 1.5):
                    break
        else:
            self.get_logger().info("getColor() called with unknown color name %s, defaulting to blue", color)
            result.r = 0.1
            result.g = 0.1
            result.b = 0.8

        return result 

    def getRandomColor(self):
        """
        Get a random color.
        @return color (ColorRGBA)
        """

        # Make a list of the color names to choose from
        all_colors = []
        all_colors.append('red')
        all_colors.append('green')
        all_colors.append('blue')
        all_colors.append('grey')
        all_colors.append('white')
        all_colors.append('orange')
        all_colors.append('yellow')
        all_colors.append('brown')
        all_colors.append('pink')
        all_colors.append('lime_green')
        all_colors.append('purple')

        # Chose a random color name
        rand_num =  random.randint(0, len(all_colors) - 1)
        rand_color_name = all_colors[rand_num]

        return rand_color_name
    


    def publishArrow(self, pose, color, scale, lifetime=None):
        if (self.muted == True):
            return True
        
        if (type(pose) == numpy.matrix) or (type(pose) == numpy.ndarray):
            arrow_pose = self.mat_to_pose(pose)
        elif type(pose) == Pose:
            arrow_pose = pose
        else:
            self.get_logger().info("Pose is unsopported type %s in publishArrow()", type(pose).__name__)
            return False
        
        if type(scale) == Vector3:
            arrow_scale = scale
        elif type(scale) == float:
            arrow_scale = Vector3(scale, 0.1*scale, 0.1*scale)
        else:
            self.get_logger().info("Scale is unsupported type %s in publishArrow()", type(scale).__name__)
            return False
        
        self.arrow_marker.id += 1

        arrow_marker = self.arrow_marker

        if lifetime == None:
            arrow_marker.lifetime = Duration(0.0)
        else:
            arrow_marker.lifetime = Duration(lifetime)
        
        arrow_marker.header.stamp = self.get_clock().now()

        arrow_marker.pose = arrow_pose

        arrow_marker.scale = arrow_scale

        arrow_marker.color = self.getColor(color)

        return self.publishMarker(arrow_marker)

    def mat_to_pose(mat):
        pose = Pose()
        pose.position.x = mat[0,3]
        pose.position.y = mat[1,3]
        pose.position.z = mat[2,3]
        quat = quaternion_from_matrix(mat)
        pose.orientation.x = quat[0]
        pose.orientation.y = quat[1]
        pose.orientation.z = quat[2]
        pose.orientation.w = quat[3]

        return pose
    