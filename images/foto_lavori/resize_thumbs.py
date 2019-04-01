from PIL import Image
import os

target_dir = "5"
percent = 0.25

for dir_name in os.listdir("."):
	if dir_name[0] == target_dir:
		for file_name in os.listdir(dir_name+"/thumbs"):
			print(file_name)
			img = Image.open(dir_name+"/thumbs/"+str(file_name))
			hsize = int((float(img.size[0]) * float(percent)))
			vsize = int((float(img.size[1]) * float(percent)))
			img = img.resize((hsize, vsize), Image.ANTIALIAS)
			img.save(dir_name+"/thumbs/"+str(file_name))
		