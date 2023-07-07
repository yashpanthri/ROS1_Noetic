#!/usr/bin/env python

import rospy
import sys
from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse
from rospy.service import ServiceException

def rectangle_area_client(w, h):
    rospy.wait_for_service("calculate_area_of_rectangle")
    try:
        area_object = rospy.ServiceProxy("calculate_area_of_rectangle", RectangleAreaService)
        resp_serv = area_object(w, h)
        return resp_serv.area
    except rospy.ServiceException(e):
        print("Service call failed: %s" %e)


def usage():
    return


if __name__ == "__main__":
    if len(sys.argv) == 3:
        w = float(sys.argv[1])
        h = float(sys.argv[2])
    else:
        print("%s[x y]"% sys.argv[0])
        sys.exit(1)
    print("Requesting %s * %s" %(w, h))
    area_received = rectangle_area_client(w, h)
    print("%s * %s = %s" %(w, h, area_received))
