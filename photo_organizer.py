
#!/usr/bin/python


import sys
import os
import shutil
sys.path.insert(0, os.path.join('.','ExifRead-2.1.2'))

import EXIF


def main():
	dates = {}
	for filename in os.listdir("."):
		
		
		if filename.endswith(".jpg") or filename.endswith(".JPG"):
			cur_file = os.path.join('.', filename)
			with open(cur_file, 'rb') as fh:
				tags = EXIF.process_file(fh, stop_tag="EXIF DateTimeOriginal")
				if "EXIF DateTimeOriginal" in tags:
					dateTaken = str(tags["EXIF DateTimeOriginal"]).split()[0]
					
					if dateTaken in dates:
						temp_list = dates[dateTaken]
						temp_list.append(cur_file)
						dates[dateTaken] = temp_list
					else:
						temp_list = []
						temp_list.append(cur_file)
						dates[dateTaken] = temp_list
	
	
	for k in dates:
		year = k.split(':')[0]
		month = k.split(':')[1]
		day = k.split(':')[2]
		filename = os.path.join('.', day+'-'+month+'-'+year)
		if not os.path.exists(filename):
			os.makedirs(filename)
		
		for f in dates[k]:
			cur_file = os.path.join('.', f)
			to_move_file = os.path.join('.',filename,f)
			shutil.copy(cur_file, to_move_file)
		
		
if __name__ == '__main__':
  main()