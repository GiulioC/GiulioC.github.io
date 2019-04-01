import numpy as np
import os, sys
import random

target_dir = "5" #folder number
sub_dir = "fulls" #fulls or thumbs
randomize = False #True to shuffle photos

temp_pics = False
for dir_name in os.listdir("."):
	if dir_name[0] == target_dir:

		for file_name in os.listdir(os.path.join(dir_name,sub_dir)):
			if file_name[:3] == "pic":
				os.rename(os.path.join(dir_name,sub_dir,file_name), os.path.join(dir_name,sub_dir,"temp"+str(file_name)))
				temp_pics = True

		file_names = os.listdir(os.path.join(dir_name,sub_dir))
		num_files = len(file_names)

		s = np.arange(num_files)
		if randomize:
			random.shuffle(s)

		count = 0

		if temp_pics:
			counter = 0
			while True:
				try:
					os.rename(os.path.join(dir_name,sub_dir,"temppic"+str(counter)+".jpg"), os.path.join(dir_name,sub_dir,"pic"+str(count)+".jpg"))
					count += 1
					counter += 1
					print(count, num_files)
					if count == num_files:
						sys.exit(0)
				except FileNotFoundError:
					counter += 1
		else:
			for num, file_name in zip(s,file_names):
				print(file_name)
				os.rename(os.path.join(dir_name,sub_dir,file_name), os.path.join(dir_name,sub_dir,"pic"+str(num)+".jpg"))
				count += 1
		