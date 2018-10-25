from PIL import Image
import os

percent = 1

for file_name in os.listdir("../foto/"):
	print(file_name)
	img = Image.open("../foto/"+str(file_name))
	hsize = int((float(img.size[0]) * float(percent)))
	vsize = int((float(img.size[1]) * float(percent)))
	img = img.resize((hsize, vsize), Image.ANTIALIAS)
	img.save(file_name)
		