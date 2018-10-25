import numpy as np
import os

for file_name in os.listdir("."):
	if file_name[:3] == "pic":
		os.rename(file_name, "temp"+str(file_name))

file_names = os.listdir(".")
numbers = np.arange(len(file_names))
np.random.shuffle(numbers)

for num,file_name in enumerate(file_names):
	if file_name[-3:] == "jpg":
		os.rename(file_name, "pic"+str(numbers[num])+".jpg")
		