#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist      
import time
def    walker():
    rospy.init_node('Turtle_mower_py', anonymous=True)
    pub = rospy.Publisher('cmd_vel', Twist , queue_size=1000)
    rate = rospy.Rate( 1 ) # 10hz
    move_cmd = Twist()
    move_cmd.linear.x = 1.0
    move_cmd.angular.z = 1.0
    counter=0
    while not rospy.is_shutdown():
	print  ("counter = %d"%counter)
	Q=mysum(linear(counter) , anguler(counter) )
	print (Q) 
	
	pub.publish(Q  )
    	pub.publish(Q  )
	
        rate.sleep()
        counter=counter+1


def    linear(Direction):
    move_cmd = Twist()
    if Direction%2 >0:
	move_cmd.linear.x = 3.0
    else:
	move_cmd.linear.x = -3.0

    return move_cmd
def    anguler(Direction):
    move_cmd = Twist()
    if Direction%2 >0:
	move_cmd.angular.z = 1.57
    else:
	move_cmd.angular.z = -1.57

    return move_cmd

def   mysum(linear , angular ):
    move_cmd = Twist()
    move_cmd.linear.x = linear.linear.x + angular.linear.x 
    move_cmd.linear.y = linear.linear.y + angular.linear.y
    move_cmd.linear.z = linear.linear.z + angular.linear.z
    move_cmd.angular.x = linear.angular.x + angular.angular.x 
    move_cmd.angular.y = linear.angular.y + angular.angular.y
    move_cmd.angular.z = linear.angular.z + angular.angular.z
    return move_cmd


if __name__ == '__main__':
    try:
        walker()
    except rospy.ROSInterruptException:
        pass


