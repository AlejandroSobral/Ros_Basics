#!/usr/bin/env python3
import rospy as ry

if __name__ == '__main__':
    ry.init_node("test_node")

    ry.loginfo("Hola hdp")

    rate = ry.Rate(10)

    while not ry.is_shutdown():


        ry.loginfo