#create publisher
imu_pub = rospy.Publisher('imu/data', Imu, queue_size=1)
#init node and set rate
rospy.init_node('imu_talker', anonymous=True)
rate = rospy.Rate(10) # 10hz

while not rospy.is_shutdown():
    #PLACEHOLDER TO GET DATA FROM IMU

    #create message and header
    imu = Imu()
    imu.header.stamp = rospy.Time.now()
    imu.header.frame_id = 'imu'

    #put data into the message
    imu.orientation = quaternion
    imu.angular_velocity = ang_vel 
    imu.linear_acceleration = lin_acc

    #publish message
    imu_pub.publish(imu)

    #sleep at known rate
    rate.sleep()
