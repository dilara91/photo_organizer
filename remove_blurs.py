#!/usr/bin/python

#http://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/

import sys
import os
import shutil
import cv2
import numpy

def rm_blur():
		
	for dirname,dirnames,filenames in os.walk('.'):
		for f in filenames:
			if f.endswith(".jpg") or f.endswith(".JPG"):
				cur_file = os.path.join(dirname,f)
				image = cv2.imread(cur_file)
				gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
				var = variance_of_laplacian(gray)
				print str(var)
				if var < 100:
					fname = f.split('.')[0]+'_blur.jpg'
					to_move_file = os.path.join(dirname,fname)
					shutil.move(cur_file, to_move_file)
	
	print 'find blurs'
def variance_of_laplacian(gray):
	laplace = cv2.Laplacian(gray,3)
	var = numpy.var(laplace)
	return var
if __name__ == '__main__':
  rm_blur()