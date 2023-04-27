#!/usr/bin/env python3
import rospy as ry
from turtlesim.msg import Pose


def pose_call_handler(msg: Pose):

    ry.loginfo(msg)

if __name__ == '__main__':
    ry.init_node("turtle_pose_subsc")


    # To find out the name:
    # rosrun turtlesim turtilesim_node
    # rostopic list >> /turtle1/pose

    #Type
    # rostopic info /turtle1/pose

    pub_name = "/turtle1/pose"
    pub_type = Pose 
    callback_fun = pose_call_handler() #Point to the function that handles the input info from topic
    sub = ry.Subscriber(pub_name, pub_type, callback=callback_fun)

    ry.loginfo("Node has been started.\n")
    ry.spin() # infinite loop to work properly

