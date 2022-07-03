# robot_localation
Iam attempting to get the most basic example of robot_localization working on a raspberry pi. I am new to linux and the ROS ecosystem, so I have fought through an exceptional number of issues to get it working. The information necessary to do this seems to be somewhat fragmented or over complicated for a beginner.

In order to do the localization I am using the BNO055 IMU by bosch that outputs orientation as well as standard IMU data. I am also using two incremental encoders on the wheels of lets say a "cart." This example is as simple as it can get, There are no motors and I just want to know the position of a cart that is pushed externally.

I have the system working, and it looks like filtered odom data seems to be more accurate, but I am having trouble making sure I did everything right.

The most basic question... is this the proper way to use ekf node? In the very simpliest terms do these three codes seem correct? I have simplified them into the important components
