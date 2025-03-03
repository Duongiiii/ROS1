#!/usr/bin/env python3 
import rospy
import random
from geometry_msgs.msg import Twist 

def move_turtle(): 
    rospy.init_node('random_turtle_controller', anonymous=True) 
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        cmd = Twist()
        cmd.linear.x = random.uniform(0, 2)  # Tốc độ thẳng 0 - 2 m/s
        cmd.angular.z = random.uniform(-2, 2)  # Tốc độ quay -2 đến 2 rad/s
        pub.publish(cmd)
        rospy.loginfo(f"Moving: linear={cmd.linear.x}, angular={cmd.angular.z}")
        rate.sleep()
        
if __name__ == '__main__':
    move_turtle()
