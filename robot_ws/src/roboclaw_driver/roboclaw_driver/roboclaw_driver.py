import rclpy
from rclpy.node import Node

class RoboclawDriver(Node):
    def __init__(self):
        super().__init__('roboclaw_driver')
        self.get_logger().info('Roboclaw driver node started.')
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Roboclaw node heartbeat.')

def main(args=None):
    rclpy.init(args=args)
    node = RoboclawDriver()
    rclpy.spin(node)
    rclpy.shutdown()
