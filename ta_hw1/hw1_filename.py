#! /usr/bin/python3

'''
creates the filename for a homework 1 text file
'''

import re
import sys
import os
import os.path

#--------------------------------------------------------------------------------------------------
   
if len(sys.argv) < 4:
    print("Usage: " + os.path.basename(sys.argv[0]) + " COURSE_ID FIRST_NAME  LAST_NAME")
    sys.exit(1)

course_id  = sys.argv[1].lower()
first_name = sys.argv[2].lower()
last_name  = sys.argv[3].lower().replace(" ","_")

#--------------------------------------------------------------------------------------------------
if course_id not in ["it116", "it117", "it244"]:
    print(course_id + "is not a valid course ID")
    sys.exit()

print(last_name + "_" + first_name + "_01_hw_" + course_id + ".txt")
