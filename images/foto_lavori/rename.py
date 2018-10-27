import numpy as np
import os, sys

target_dir = "3"

temp_pics = False

for dir_name in os.listdir("."):
	if dir_name[0] == target_dir:
		for file_name in os.listdir(dir_name+"/fulls"):
			if file_name[:3] == "pic":
				os.rename(dir_name+"/fulls/"+file_name, dir_name+"/fulls/temp"+str(file_name))
				temp_pics = True

		file_names = os.listdir(dir_name+"/fulls")

		count = 0

		if temp_pics:
			num_files = os.listdir(dir_name+"/fulls")
			counter = 0
			while True:
				try:
					os.rename(dir_name+"/fulls/temppic"+str(counter)+".jpg", dir_name+"/fulls/pic"+str(count)+".jpg")
					count += 1
					counter += 1
					if count == num_files:
						sys.exit(0)
				except FileNotFoundError:
					counter += 1
		else:
			for num,file_name in enumerate(file_names):
				print(file_name)
				os.rename(dir_name+"/fulls/"+file_name, dir_name+"/fulls/pic"+str(count)+".jpg")
				count += 1
		