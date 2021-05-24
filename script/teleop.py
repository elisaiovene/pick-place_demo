#!/usr/bin/env python

try:
	import tkinter
except ImportError:
	import Tkinter as tkinter

from psmIK import *
from ambf_client import Client
from psm_arm import PSM
import time
import rospy
from PyKDL import Frame, Rotation, Vector
from argparse import ArgumentParser
import obj_control_gui
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Float32
import numpy

#global v_x,v_y
vel= Twist()
scroll = Float32()
grip = Float32()
change= Float32()
count = 0
c = Client()
c.connect()
time.sleep(2.0)
b1= c.get_obj_handle('psm1/baselink')
time.sleep(1.0)
b2 = c.get_obj_handle('psm2/baselink')

def mouse(msg):
	

def mouse_scroll(data):
	
	

def mouse_grip(data1):
	
def mouse_change(data2):
	
	
	

def teleop(): 
	global v_x,v_y
	
	mouse_sub = rospy.Subscriber("/mouse_vel",Twist,mouse)
	mouse_sub_scroll = rospy.Subscriber("/mouse_scroll",Float32,mouse_scroll)
	mouse_sub_grip = rospy.Subscriber("/mouse_grip",Float32,mouse_grip)
	mouse_sub_change = rospy.Subscriber("/mouse_change",Float32,mouse_change)
	b1.set_joint_pos('toolrolllink-toolpitchlink',0.0)
	time.sleep(1.0)
	b1.set_joint_pos('toolpitchlink-toolyawlink',0.5)
	time.sleep(1.0)
	b1.set_joint_pos('maininsertionlink-toolrolllink',0.0)
	b2.set_joint_pos('toolrolllink-toolpitchlink',0.0)
	time.sleep(1.0)
	b2.set_joint_pos('toolpitchlink-toolyawlink',0.5)
	time.sleep(1.0)
	b2.set_joint_pos('maininsertionlink-toolrolllink',0.0)
	print("ready for use")

	while not rospy.is_shutdown():

		if (change.data %2) == 0:
			b1.set_joint_pos('baselink-yawlink',b1.get_joint_pos('baselink-yawlink')+float(vel.linear.y)/2)
			b1.set_joint_pos('yawlink-pitchbacklink',b1.get_joint_pos('yawlink-pitchbacklink')-float(vel.linear.x)/2)
			b1.set_joint_pos('pitchendlink-maininsertionlink',scroll.data)
			#b1.set_joint_vel('pitchendlink-maininsertionlink',scroll.data)
			b1.set_joint_pos('toolyawlink-toolgripper1link',grip.data)
			b1.set_joint_pos('toolyawlink-toolgripper2link',grip.data)

		else:
			b2.set_joint_pos('baselink-yawlink',b2.get_joint_pos('baselink-yawlink')+float(vel.linear.y)/2)
			b2.set_joint_pos('yawlink-pitchbacklink',b2.get_joint_pos('yawlink-pitchbacklink')-float(vel.linear.x)/2)
			b2.set_joint_pos('pitchendlink-maininsertionlink',scroll.data)
			#b2.set_joint_vel('pitchendlink-maininsertionlink',scroll.data)
			b2.set_joint_pos('toolyawlink-toolgripper1link',grip.data)
			b2.set_joint_pos('toolyawlink-toolgripper2link',grip.data)


		



if __name__ == '__main__':
	teleop()

