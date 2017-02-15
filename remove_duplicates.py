#!/usr/bin/python

#http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html

import sys
import os
import shutil
import cv2
import numpy as np
import re

def rm_similar():
	dir_list = [o for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
	
	for d in dir_list:
		similar = {}
		dir_name = os.path.join('.',d)
		d_list = os.listdir(dir_name)
		comparison_file = os.path.join(dir_name,d_list[0])
		for i in xrange(1,len(d_list)-1):
			cur_file = os.path.join(dir_name,d_list[i])
			if not cur_file.endswith(".jpg") and not cur_file.endswith(".JPG"):
				continue
			mean = similarity(comparison_file,cur_file)
			print mean
			if mean<60:
				if comparison_file in similar:
					temp_list = similar[comparison_file]
					temp_list.append(cur_file)
					similar[comparison_file] = temp_list
				else:
					temp_list = []
					temp_list.append(cur_file)
					similar[comparison_file] = temp_list
			else:
				comparison_file = cur_file
	
		count = 1		
		for k in similar.keys():
			f_list = similar[k]
			new_file = os.path.join(dir_name,str(count))
			if not os.path.exists(new_file):
				os.makedirs(new_file)
			to_move_key = os.path.join(new_file,os.path.basename(k))
			shutil.move(k, to_move_key)
			count = count + 1
			for f in f_list:
				to_move_file = os.path.join(new_file,os.path.basename(f))
				shutil.move(f, to_move_file)

	print 'found duplicates'
def similarity(im1,im2):
	img1 = cv2.imread(im1,0) 
	img2 = cv2.imread(im2,0) 

	# Initiate SIFT detector
	orb = cv2.ORB()

	# find the keypoints and descriptors with SIFT
	kp1, des1 = orb.detectAndCompute(img1,None)
	kp2, des2 = orb.detectAndCompute(img2,None)
	
	# create BFMatcher object
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

	# Match descriptors.
	matches = bf.match(des1,des2)

	# Sort them in the order of their distance.
	#matches = sorted(matches, key = lambda x:x.distance)

	print len(matches)
	if len(matches) is 0:
		return 100
	lis = [m.distance for m in matches]
	
	return np.mean(lis)
	
if __name__ == '__main__':
  rm_similar()