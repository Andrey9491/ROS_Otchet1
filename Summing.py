#!/usr/bin/env python

'''from study_pkg.srv import Poly, PolyResponse
import rospy

def handle_poly_srv(req):
    result = req.a + req.b
    rospy.loginfo("Returning Summing [%d + %d = %d]" % (req.a, req.b, result))
    
    #resp = PolyResponse()
    #resp.sum = result
    
    #return resp

def poly_server():
    rospy.init_node('poly_server')
    s = rospy.Service('poly', Poly, handle_poly_srv)
    rospy.loginfo("Ready to calc sum.")
#    rospy.spin()

poly_server()'''

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
from std_msgs.msg import Int64

def callback(msg):
    rospy.loginfo("i heard speed %d; steer %d", msg.x, msg.y)
    result = msg.x + msg.y
    pub = rospy.Publisher('chat_Summing', Int64, queue_size=10)
    pub.publish(result)
    rospy.loginfo("I send %d", result)



rospy.init_node('Summing')
rospy.Subscriber('chat_Polynomial', Control, callback, queue_size=10)
rospy.spin()

#############
'''pub = rospy.Publisher('chat_Polynomial', Control, queue_size=10)
rate = rospy.Rate(10)

def start_talker():
    msg = Control()
    x = msg.x
    y = msg.y
    while not rospy.is_shutdown():
        rospy.loginfo("speed %d, steer %d", msg.x, msg.y)

        msg = Control()
        x = msg.x 
        y = msg.y ** 2
        msg.x = x
        msg.y = y
        pub.publish(msg)
        
        rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')'''