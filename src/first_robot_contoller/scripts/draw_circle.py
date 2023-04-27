#!/usr/bin/env python3
import rospy as ry
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    ry.init_node("draw_circle")
    ry.loginfo("Node has been created.")
    

    # To find out the name:
    # rosrun turtlesim turtilesim_node
    # rostopic list >> /turtle1/cmd_vel

    #Type
    # rostopic info /turtle1/cmd_vel
    # rosmsg show geometry_msgs/Twist -> Find out parameters it has

    pub_name = "/turtle1/cmd_vel"
    pub_type = Twist # "geometry_msgs/Twist"
    queue_size = 10 #Buffer size or smth like
    pub = ry.Publisher(pub_name, pub_type, queue_size=queue_size)

    rate = ry.Rate(2) # 2Hz

    while not ry.is_shutdown():
        # publish cmd_vel
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 0.4
        pub.publish(msg)
        rate.sleep()
