#!/usr/bin/env python
# Where the IoTSensor message type contains 
# int32 id
# string name
# float32 temperature
# float32 humidity
import rospy
from ros_essentials_cpp.msg import IoTSensor

def IoTSensor_Callback(IoTSensor_message):
    rospy.loginfo("New IoT Sensor data recieved: %d, %s, %.2f, %.2f", IoTSensor_message.id, IoTSensor_message.name, IoTSensor_message.temperature, IoTSensor_message.humidity)

def IoTSensor_subscriber():
    rospy.init_node('IoTSensor_subscriber_node', anonymous=True)
    rospy.Subscriber("IoTSensor_topic", IoTSensor, IoTSensor_Callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        IoTSensor_subscriber()
    except rospy.ROSInterruptException:
        pass
