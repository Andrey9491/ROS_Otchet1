#!/usr/bin/env python

import rospy
from study_pkg.msg import Control
from std_msgs.msg import Int64

def callback(msg):
    rospy.loginfo("i heard result %d", msg.data)

rospy.init_node('Request')
pub = rospy.Publisher('chat_Request', Control, queue_size=10)
rate = rospy.Rate(1)

def start_talker():
    msg2 = Control()
    msg2.x = int(input("Введите х: "))
    msg2.y = int(input("Введите у: "))
    while not rospy.is_shutdown():
        pub.publish(msg2)
        rospy.Subscriber('chat_Summing', Int64, callback, queue_size=10)
        rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')