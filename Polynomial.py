#!/usr/bin/env python
'''
from study_pkg.srv import Poly, PolyRequest, PolyResponse
import rospy

def handle_poly_srv(req):
    req.a = req.x 
    req.b = req.y ** 2
    rospy.loginfo("Returning Polynomial [%d = %d; %d^2 = %d]" % (req.x, req.a, req.y, req.b))
    rospy.loginfo("Handle успешно")
    #resp = PolyResponse()
    #resp.sum = 0
    
    #return resp

def poly_server():
    rospy.init_node('poly_server1')
    s = rospy.Service('poly', Poly, handle_poly_srv)
    rospy.loginfo("Ready to calc polynomial.")
    
    poly_server()
    rospy.wait_for_service('poly')
    try:
        poly_srv = rospy.ServiceProxy('poly', Poly)
        req = PolyRequest(a=12, b=15)
        resp = poly_srv(req)
    except rospy.ServiceException:
        rospy.logerr("Service call failed: %s" % e)
    
    rospy.spin()'''

#!/usr/bin/env python
import rospy
from study_pkg.msg import Control

def callback(msg):
    
    rospy.loginfo("i heard x %d; y %d", msg.x, msg.y)
    msg2 = Control()
    msg2.x = msg.x
    msg2.y = msg.y ** 2
    pub = rospy.Publisher('chat_Polynomial', Control, queue_size=10)
    pub.publish(msg2)
    rospy.loginfo("I send %d, %d", msg2.x, msg2.y)

rospy.init_node('Polynomial')
rospy.Subscriber('chat_Request', Control, callback, queue_size=10)

rospy.spin()
#############
'''pub = rospy.Publisher('chat_Polynomial', Control, queue_size=10)
rate = rospy.Rate(1)

def start_talker():
    msg2 = Control()
    x = msg2.x
    y = msg2.y ** 2
    while not rospy.is_shutdown():
        rospy.loginfo("speed %d, steer %d", msg2.x, msg2.y)

        msg = Control()
        x = msg2.x 
        y = msg2.y ** 2
        msg2.x = x
        msg2.y = y
        pub.publish(msg2)
        
        rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')'''
