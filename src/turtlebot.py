#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist      
import time

def walk(direction):
    move_cmd = Twist()
    move_cmd.linear.x = direction
    move_cmd.angular.z = 0.0
    return move_cmd

def rotate(angle):
    move_cmd = Twist()
    move_cmd.linear.x = 0.1
    move_cmd.angular.z = angle
    return move_cmd


def main():
    rospy.init_node('Turtle_control_py' , anonymous= True)
    pub = rospy.Publisher( '/cmd_vel' , Twist , queue_size = 1000)
    rate = rospy.Rate(1)
	
    while not rospy.is_shutdown():

        time.sleep(1)
        pub.publish(walk(0.3))
        time.sleep(5)
        pub.publish(rotate(0.7))
        time.sleep(4.5)
        pub.publish(walk(0.3))
        time.sleep(5)
        pub.publish(rotate(-0.7))
        time.sleep(3.5)
        rate.sleep()



if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
