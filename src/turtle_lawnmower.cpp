#include "ros/ros.h"
#include <geometry_msgs/Twist.h>
#include <iostream>
#include <unistd.h>
unsigned int microsecond = 1000000;

using namespace std;
void walk(float v);
void rotate();
void rotate_anticlock();

ros::Publisher my_publisher;
int counter = 0;
int omar=2;
int main(int argc, char **argv)
{
	ros::init(argc, argv, "turtle_lawnmower");
	ros::NodeHandle mynode;
	bool move;
	my_publisher = mynode.advertise<geometry_msgs::Twist>("cmd_vel", 1000);
	ros::Rate loop_rate(5);
	while(ros::ok()){

	if(counter == 0){
		for(int i = 0; i<4; i++){
	cout<<"Move Turtle Front";
	usleep(2.5 * microsecond);
	walk(1.3);
	counter = 1;	
}
}
	else {
		for(int m = 0; m<8; m++){
	cout<<"Move Turtle Front";
	usleep(2.5 * microsecond);
	walk(1.21);
	counter = 1;
}
}

		for(int y = 0; y<2; y++){
	cout<<"Move Turtle Front";
	usleep(2.5 * microsecond);
	rotate();
	
}
		for(int f = 0; f<8; f++){
	cout<<"Move Turtle Front";
	usleep(1 * microsecond);
	walk(1.21);
	
}
		for(int g = 0; g<2; g++){
	cout<<"Move Turtle Front";
	usleep(2.5 * microsecond);
	rotate_anticlock();
	
}


}
return 0;
}

void walk(float v){


geometry_msgs::Twist vel_msg;
vel_msg.linear.x = v;
my_publisher.publish(vel_msg);

}
void rotate(){


geometry_msgs::Twist vel_msg;
vel_msg.linear.x = 0.3;
vel_msg.linear.y = 0;
vel_msg.linear.z = 0;
vel_msg.angular.x = 0;
vel_msg.angular.y = 0;
vel_msg.angular.z = -1.57;
my_publisher.publish(vel_msg);

}

void rotate_anticlock(){
geometry_msgs::Twist vel_msg;
vel_msg.linear.x = 0.3;
vel_msg.linear.y = 0;
vel_msg.linear.z = 0;
vel_msg.angular.x = 0;
vel_msg.angular.y = 0;
vel_msg.angular.z = 1.57;
my_publisher.publish(vel_msg);

}

