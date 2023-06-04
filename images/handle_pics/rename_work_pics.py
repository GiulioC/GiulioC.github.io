import argparse
import os
import random
import sys

import numpy as np


def rename_photos(dir_name, sub_dir, shuffle):
	temp_pics = False

	for file_name in os.listdir(os.path.join(dir_name,sub_dir)):
		if file_name[:3] == "pic":
			os.rename(os.path.join("../foto_lavori", dir_name, sub_dir, file_name), os.path.join("../foto_lavori", dir_name, sub_dir, "temp"+str(file_name)))
			temp_pics = True

	file_names = os.listdir(os.path.join(f"../{dir_name}", sub_dir))
	file_names.sort()
	num_files = len(file_names)

	s = np.arange(num_files)
	if shuffle:
		random.shuffle(s)

	count = 0

	if temp_pics:
		counter = 0
		while True:
			try:
				os.rename(os.path.join("../foto_lavori", dir_name, sub_dir, "temppic"+str(counter)+".jpg"), os.path.join("../foto_lavori", dir_name, sub_dir, "pic"+str(count)+".jpg"))
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
			os.rename(os.path.join("../foto_lavori", dir_name, sub_dir, file_name), os.path.join("../foto_lavori", dir_name, sub_dir, "pic"+str(num)+".jpg"))
			count += 1

if __name__ == '__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument('--job_num', required=True)
	argparser.add_argument('--photo_dir', required=True)
	argparser.add_argument('--shuffle', action='store_true')
	args = argparser.parse_args()

	print(args)

	rename_photos(args.job_num, args.photo_dir, args.shuffle)
		