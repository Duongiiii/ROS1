#!/usr/bin/env python3
import sys, termios, tty, select
import rospy
from geometry_msgs.msg import Twist

settings = termios.tcgetattr(sys.stdin)
key_bindings = {
    'w': (5, 0),   # Tiến
    's': (-6, 0),  # Lùi
    'a': (0, 1.5),   # Quay trái
    'd': (0, -3),  # Quay phải
    'q': (0, 0)      # Dừng
}

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main():
    rospy.init_node('keyboard_turtle_control')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    while not rospy.is_shutdown():
        key = getKey()
        if key in key_bindings:
            twist = Twist()
            twist.linear.x, twist.angular.z = key_bindings[key]
            pub.publish(twist)
        if key == '\x03':  # Ctrl+C để thoát
            break

if __name__ == '__main__':
    main()
