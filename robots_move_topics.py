

#Subscribe for the topic that will show the location of the robot

#Publisher to the topic that will make the robot move

#What is the topic of the position
#What is the topic that makes the robot move

#!/usr/bin/env.python
#license removed for brevity
import rospy
from geometry_msgs.msg import Twist

def move():
    #create a new publisher, we specify the topic name, then type of message then the queue size
    speed_publisher = rospy.Publisher('/turtle1/cmd_vel', String, queue_size=10)
    rospy.init_node('talker',anonymous=True)
    rate = rospy.Rate(1)
    i=0
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 1.0

        rospy.loginfo(hello_str)
        speed_publisher.publish(hello_str)
        rate.sleep()
        i+=1

if __name__ = '__main__'
try:
    move():
except ROSInterruptException:
    pass