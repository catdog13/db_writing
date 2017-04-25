#!/usr/bin/env python3
import os
import time

file_info = os.stat('/media/tom/arrrrrrrrr/Movies/Terminator Genisys (2015)/Terminator Genisys.mp4')
# print(file_info.st_ctime)
ucttime = time.gmtime(file_info.st_ctime)
localtime = time.localtime(file_info.st_ctime)
print(localtime)
