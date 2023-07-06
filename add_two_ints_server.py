#!/usr/bin/env python

import rospy
import time
from ros_essentials_cpp.srv import AddTwoInts
from ros_essentials_cpp.srv import AddTwoIntsRequest 
from ros_essentials_cpp.srv import AddTwoIntsResponse

def handle_two_ints(req):
    print("Returning [%s + %s = %s]" % ( req.a, req.b, (req.a +req.b) ) )
    time.sleep(5)
    return AddTwoIntsResponse(req.a +req.b)



def add_two_ints_server():
    rospy.init_node("add_two_ints_server")
    s= rospy.Service("add_two_ints", AddTwoInts, handle_two_ints)
    print("Ready to add two ints")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()