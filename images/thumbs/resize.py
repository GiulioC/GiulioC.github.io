from PIL import Image
import os

percent = 0.5

for file_name in os.listdir("../foto/"):
	if file_name == "pic8.jpg":
		img = Image.open("../foto/"+str(file_name))

		if img.size[0] > img.size[1]:
			#foto orizzontale
			hsize = int((float(img.size[0]) * float(percent)))
			vsize = int((float(img.size[1]) * float(percent)))
		else:
			#foto verticale
			hsize = int((float(img.size[0]) * float(percent)))
			vsize = int((float(img.size[1]) * float(percent)))
		img = img.resize((hsize, vsize), Image.ANTIALIAS)
		img.save(file_name)
		