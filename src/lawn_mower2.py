#!/usr/bin/env python 

import rospy
import math 
from nav_msgs.msg import Odometry
landmarks = []
landmarks.append(("cylinder1", 1.0332 ,1.276))
landmarks.append(("cylinder2", -1.214 ,-0.1513))

def distance (x1 , y1 , x2 , y2):
    xd = x1 - x2 
    yd = y1 - y2
    return math.sqrt(xd*xd + yd*yd)

def callback(msg):

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    closest_name = None
    closest_distance = None
    for l_name , l_x , l_y in landmarks:
        dist = distance(x,y , l_x , l_y)
        if closest_distance is None or dist < closest_distance: 
            closest_name = l_name 
            closest_distance = dist
    rospy.loginfo('closest: {}'.format (closest_name))
    #do somthing with closest 
def main() :
    rospy.init_node('location_node')
    rospy.Subscriber("/odom",Odometry,callback)
    rospy.spin()


if __name__ == '__main__':
    main()