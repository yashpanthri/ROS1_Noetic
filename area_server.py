#!/usr/bin/env python

import rospy
from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse
import time

def handle_area_calculation(req):
    print("Returning [ %s * %s =  %s ]" % (req.width, req.height, (req.width*req.height)))
    time.sleep(5)
    return RectangleAreaServiceResponse(req.width*req.height)

def area_of_rectangle_server():
    rospy.init_node("rectangle_area_server")
    rospy.Service("calculate_area_of_rectangle", RectangleAreaService, handle_area_calculation)
    print("Ready to calculate area of rectangle")
    rospy.spin()

if __name__ == "__main__":
    area_of_rectangle_server()