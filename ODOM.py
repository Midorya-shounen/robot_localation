#create publishers
odom_pub = rospy.Publisher("odom", Odometry, queue_size=1)
odom_broadcaster = tf.TransformBroadcaster()

#init node and rate
rospy.init_node('odom_talker', anonymous=True)
rate = rospy.Rate(10) # 10hz

while not rospy.is_shutdown():
    #PLACEHOLDER TO GET ODOMETRY FROM ENCODERS

    #create message and header
    odom = Odometry()
    odom.header.stamp = rospy.Time.now()
    odom.header.frame_id = "odom"

    #convert euler to quaternion
    odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)
    #broadcast transform
    odom_broadcaster.sendTransform((x, y, 0.), odom_quat,current_time,"base_link", "odom")


    # set the position
    odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))

    # set the velocity
    odom.child_frame_id = "base_link"
    odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))

    # publish the message
    odom_pub.publish(odom)

    #sleep at known rate
    rate.sleep()
