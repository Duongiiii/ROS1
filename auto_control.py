#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import random

current_msg = Pose()

def pose_callback(msg):
    global current_msg
    current_msg = msg

def main():
    rospy.init_node("auto_control", anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        vel = Twist()
        
        # Kiểm tra xem có gần tường không
        if current_msg.x < 0.8 or current_msg.x > 10.2 or current_msg.y < 0.8 or current_msg.y > 10.2:
            vel.angular.z = random.choice([-2.0, 2.0])  # Quay ngẫu nhiên trái hoặc phải
            vel.linear.x = 2.0  # Tiếp tục di chuyển
        else:
            vel.angular.z = random.uniform(-1.5, 1.5)  # Di chuyển hỗn loạn khi xa tường
            vel.linear.x = 2.5  # Tốc độ cao hơn khi không gần tường
        
        pub.publish(vel)
        rate.sleep()

if __name__ == "__main__":
    main()
