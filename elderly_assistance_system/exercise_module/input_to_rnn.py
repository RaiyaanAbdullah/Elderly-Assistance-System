# -*- coding: utf-8 -*-
"""
Created on Sun May  2 23:34:25 2021

@author: Raiyaan Abdullah
"""

import math
import os
from analyze_single_frame import get_keypoints

PI = 3.14159265

json_files_location = 'D:/Elderly Assistant External files/Exercise Videos/Openpose variations/openpose-1.7.0-binaries-win64-gpu/openpose/python/output_json_folder/'

def angle(line_a, line_b):
    a_x0, a_y0, a_x1, a_y1 = line_a
    b_x0, b_y0, b_x1, b_y1 = line_b
    #exceptions if either line is parallel to y axis
    if (a_x1 - a_x0) == 0 and (b_x1 - b_x0)==0:
        theta = 0
    
    elif (a_x1 - a_x0) == 0:
        theta = PI/2 - math.atan2((b_y1 - b_y0), (b_x1 - b_x0))

    elif (b_x1 - b_x0) == 0:
        theta = PI/2 - math.atan2((a_y1 - a_y0), (a_x1 - a_x0))
    #normal case
    else:
        
        m_a = (a_y1 - a_y0)/(a_x1 - a_x0)
        m_b = (b_y1 - b_y0)/(b_x1 - b_x0)
        tan_theta = (m_a-m_b)/(1+m_a*m_b)
        tan_theta = tan_theta if tan_theta>0 else -tan_theta
        theta = math.atan(tan_theta)
    
    theta_deg = math.degrees(theta)
    
    return theta_deg

#print (angle([-2.0,0.0,0.0,3.4641],[4.0,0.0,4.0,2.0]))
i=0
video_frames=[]
per_frame=13

for file in os.listdir(json_files_location):
    #getting keypoints
    all_keypoints= get_keypoints(json_files_location+file)
    important_parts = ["head", "abdomen", "chest", "l_hand", "l_elbow", "l_shoulder", "r_hand", "r_elbow", "r_shoulder"]
    keypoints = {key: value for key, value in all_keypoints.items() if key in important_parts}
    
    #getting lines of some body parts
    neck_line = [keypoints['head']['X'],keypoints['head']['Y'],keypoints['chest']['X'],keypoints['chest']['Y']]
    body_line = [keypoints['chest']['X'],keypoints['chest']['Y'],keypoints['abdomen']['X'],keypoints['abdomen']['Y']]
    r_arm_line = [keypoints['r_shoulder']['X'],keypoints['r_shoulder']['Y'],keypoints['r_elbow']['X'],keypoints['r_elbow']['Y']]
    r_forearm_line = [keypoints['r_elbow']['X'],keypoints['r_elbow']['Y'],keypoints['r_hand']['X'],keypoints['r_hand']['Y']]
    l_arm_line = [keypoints['l_shoulder']['X'],keypoints['l_shoulder']['Y'],keypoints['l_elbow']['X'],keypoints['l_elbow']['Y']]
    l_forearm_line = [keypoints['l_elbow']['X'],keypoints['l_elbow']['Y'],keypoints['l_hand']['X'],keypoints['l_hand']['Y']]

    #getting angles of parts with respect to body  
    keypoints['neck_angle']= angle(neck_line, body_line)
    keypoints['r_arm_angle'] = angle(r_arm_line, body_line)
    keypoints['r_forearm_angle'] = angle(r_forearm_line, body_line)
    keypoints['l_arm_angle'] = angle(l_arm_line, body_line)
    keypoints['l_forearm_angle'] = angle(l_forearm_line, body_line)


    if i % per_frame == 0:
        video_frames.append(keypoints)        

    i=i+1