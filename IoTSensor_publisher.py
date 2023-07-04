#!/usr/bin/env python
# Where the IoTSensor message type contains 
# int32 id
# string name
# float32 temperature
# float32 humidity
import rospy
from ros_essentials_cpp.msg import IoTSensor 
import random

def talker():
    pub = rospy.Publisher('IoTSensor_topic', IoTSensor, queue_size = 10)

    rospy.init_node("IoTSensor_publisher_node", anonymous=True)

    rate = rospy.Rate(1)

    i=0
    while not rospy.is_shutdown():
        sensor_data = IoTSensor()
        sensor_data.id = 1
        sensor_data.name = "iot_parking_01"
        sensor_data.temperature = 24.33 + random.random() *2
        sensor_data.humidity = 33.41 + random.random()*2
        rospy.loginfo("I publish")
        rospy.loginfo(sensor_data)
        pub.publish(sensor_data)
        rate.sleep()
        i=i+1

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
