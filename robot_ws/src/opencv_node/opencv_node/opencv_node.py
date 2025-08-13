import rclpy
from rclpy.node import Node

class OpenCVNode(Node):  # ← THIS WAS MISSING
    def __init__(self):
        super().__init__('opencv_node')
        self.get_logger().info("OpenCV node is running.")

def main(args=None):
    rclpy.init(args=args)
    node = OpenCVNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
