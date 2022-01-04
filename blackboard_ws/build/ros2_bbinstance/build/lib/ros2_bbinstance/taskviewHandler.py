from python_qt_binding import QtWidgets, QtCore
from ros2_bbinstance.taskview import Ui_handler, Ui_MainWindow
import sys
import rclpy



def main(args=None):
    
    rclpy.init(args=args)
    handler = Ui_handler('ui_handler', ui)
    rclpy.spin_once(ui)
    rclpy.spin(handler)
    
    
if __name__ == "__main__":
    main()
    