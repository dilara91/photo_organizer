
#!/usr/bin/python


import sys
import os
import shutil
import separate_dates as sd
import remove_blurs as rb
import remove_duplicates as rd

def main():
	sd.separate()
	rd.rm_similar()
	rb.rm_blur()
	
	
if __name__ == '__main__':
  main()