#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_callback(msg):
    # Giới hạn va chạm với tường (tường ở khoảng 0.3 - 0.4m)
    warning_threshold = 0.4
    min_x, max_x = 0.3, 10.7
    min_y, max_y = 0.3, 10.7

    # Hiển thị vị trí hiện tại
    rospy.loginfo(f"Rùa tại: x={msg.x:.2f}, y={msg.y:.2f}")

    # Kiểm tra nếu sắp va chạm
    if msg.x < min_x or msg.x > max_x or msg.y < min_y or msg.y > max_y:
        rospy.logwarn("Rùa sắp chạm tường!")

def listener():
    rospy.init_node('pose_listener', anonymous=True)
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
