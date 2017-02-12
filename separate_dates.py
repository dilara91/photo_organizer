#!/usr/bin/python


import sys
import os
import shutil

sys.path.insert(0, os.path.join('.','ExifRead'))

import EXIF as exif

def separate():
	for filename in os.listdir("."):		
		if filename.endswith(".jpg") or filename.endswith(".JPG"):
			cur_file = os.path.join('.', filename)
			with open(cur_file, 'rb') as fh:
				tags = exif.process_file(fh, stop_tag="EXIF DateTimeOriginal")
				if "EXIF DateTimeOriginal" in tags:
					dateTaken = str(tags["EXIF DateTimeOriginal"]).split()[0]
					year = dateTaken.split(':')[0]
					month = dateTaken.split(':')[1]
					day = dateTaken.split(':')[2]
					f = os.path.join('.', day+'-'+month+'-'+year)
					
					if not os.path.exists(f):
						os.makedirs(f)					
					
					to_move_file = os.path.join('.',f,filename)
					shutil.copy(cur_file, to_move_file)	
					
			
	
if __name__ == '__main__':
  separate()