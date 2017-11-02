# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:37:20 2017

@author: Quentin
"""
import sys
import os
import numpy as np


sys.path.append('./motion')

import math as math
import BVH as BVH
import Animation as Animation

file_name = "test.bvh"
file_path= "./data/animations/"



def distance(position1, position2):
    distance = math.sqrt((position2[0]-position1[0])**2+(position2[1]-position1[1])**2+(position2[2]-position1[2])**2)
    return distance

def treshold_check(distance1, distance2):
    activate = False
    treshold_value = 0.7
    if distance1 <= treshold_value and distance2 <= treshold_value:
        activate = True
    return activate

file_object = open(file_path+file_name, 'r')

anim, names, frametime = BVH.load(file_path+file_name)
frames_number = len(anim)
global_positions = Animation.positions_global(anim)


left_foot_id = 0
left_toe_id = 0
right_foot_id = 0
right_toe_id = 0


for i in range(0, len(names)):
    if names[i] == "LeftFoot" :
        left_foot_id = i
    if names[i] == "LeftToeBase" :
        left_toe_id = i
        
    if names[i] == "RightFoot" :
        right_foot_id = i
    if names[i] == "RightToeBase" :
        right_toe_id = i

switch = False

for i in range(1, frames_number-1):
    if switch:
        LFd = distance(global_positions[i-1][left_foot_id], global_positions[i+1][left_foot_id])
        LTd = distance(global_positions[i-1][left_toe_id], global_positions[i+1][left_toe_id])
        if treshold_check(LFd, LTd):
            print("left step detected at frame : ", i)
            switch = False
    else:
        RFd = distance(global_positions[i-1][right_foot_id], global_positions[i+1][right_foot_id])
        RTd = distance(global_positions[i-1][right_toe_id], global_positions[i+1][right_toe_id])
        if treshold_check(RFd, RTd):
            print("right step detected at frame : ", i)
            switch = True

file_object.close()


