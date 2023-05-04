#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen



def call_set_pen_service(r, g, b, width, off, service_name):
    # rosservice info /turtle1/set_pen

    try:
        service_type = SetPen
        service_set_pen = rospy.ServiceProxy(service_name, service_type) # Associate service
        response = service_set_pen(r,g,b,width,off) # Use the service itself
        #rospy.loginfo(response)
        
    except rospy.ServiceException as e:
        rospy.logwarn("Service ain't running,",e)

def pose_callback(pose: Pose):
    cmd = Twist()



    if pose.x > 9 or pose.x < 2 or pose.y > 9 or pose.y < 2:

        call_set_pen_service(r = 200, g = 0, b = 50, width= 4 , off=0, service_name=service_name)
        cmd.linear.x = 1.0
        cmd.angular.z = 1.4
    else:

        call_set_pen_service(r = 0, g = 0, b = 200, width= 4 , off=0, service_name=service_name)
        cmd.linear.x = 10.0
        cmd.angular.z = 0.0
    

    pub.publish(cmd)



if __name__ == '__main__':
    
    rospy.init_node("turtle_controller")

    service_name = "/turtle1/set_pen" # rosservice list
    rospy.wait_for_service(service_name) # Wait for service to be up. Blocking!.
    

    # Publisher
    pub_name = "/turtle1/cmd_vel"
    pub_type = Twist # "rostopic info /turtle1/cmd_vel" -> geometry_msgs/Twist"
    queue_size = 10 #Buffer size or smth like
    pub = rospy.Publisher(pub_name, pub_type, queue_size=queue_size)

    # Suscriber
    sub_name = "/turtle1/pose"
    sub_type = Pose 
    sub = rospy.Subscriber(sub_name, sub_type, callback=pose_callback)
    rospy.loginfo("Node suscriber has been started.")
    rospy.spin()

    


    #rate = rospy.Rate(2) # 2Hz