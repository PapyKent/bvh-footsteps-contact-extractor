# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:37:20 2017

@author: Quentin
"""
import sys
import os
import numpy as np


sys.path.append('./motion')


import BVH as BVH
import Animation as Animation

file_name = "test.bvh"
file_path= "./data/animations/"

file_object = open(file_path+file_name, 'r')

'''
for line in file_object:
    print (line);
'''

anims, names, frametime = BVH.load(file_path+file_name)
'''
for i in range(1, len(names)):
        print(names[i], " : ", anims[i].positions)
'''
print (anims.positions)
file_object.close()



