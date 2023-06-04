import argparse
import os
import random
import re

from PIL import Image, UnidentifiedImageError

def read_input_photos():
	photo_list = os.listdir("../foto_input")
	random.shuffle(photo_list)
	return photo_list

def resize_photos(target_res, out_dir="foto"):
	photos = []
	for file_name in read_input_photos():
		try:
			img = Image.open(os.path.join("../foto_input", file_name))
		except UnidentifiedImageError:
			continue

		img_width = img.size[0]
		img_height = img.size[1]

		portrait = True if img_height > img_width else False
		longest_res = img_height if portrait else img_width
		resize_ratio = target_res/longest_res

		if longest_res < target_res * 1.1:
			pass

		new_width = int((float(img_width) * float(resize_ratio)))
		new_height = int((float(img_height) * float(resize_ratio)))

		img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
		out_file = os.path.join(out_dir, file_name)
		img.save(out_file)
		photos.append(file_name)
		print(f"Saved {out_file}")
	return photos

def generate_html(photos):
	out_html = """				
				<div id="wrapper" class="row">
					<div class="4u 12u$(mobile)">"""
	chunk_size = int(len(photos)/3)
	for idx, photo in enumerate(photos):
		desc_ita, desc_eng = re.match("(.*)\$(.*)\.jpg", photo, re.I).groups()
		desc_ita = re.sub("[0-9]+_", "", desc_ita)
		out_html = f"""{out_html}
						<article class="item thumb">
							<a href="../images/foto/{photo}" class="image fit"><img src="../images/placeholder.jpg" data-src="../images/thumbs/{photo}" alt="" /></a>
							<header>
								<h3 class="desc-it" style="display:none">{desc_ita}</h3>
								<h3 class="desc-en" style="display:none">{desc_eng}</h3>
							</header>
						</article>"""

		if (idx+1) % chunk_size == 0 and (idx+1) != len(photos):
			out_html = f"""{out_html}
					</div>
					<div class="4u 12u$(mobile)">"""
	out_html = f"""{out_html}
					</div>
				</div>"""
	
	with open("photos.html", "w") as f:
		f.write(out_html)


if __name__ == '__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument('--target_res', default=1600)
	argparser.add_argument('--shuffle', action='store_true')
	args = argparser.parse_args()

	if args.shuffle:
		photo_list = read_input_photos()
	else:
		photo_list = resize_photos(int(args.target_res))
		resize_photos(int(args.target_res/2.5), out_dir="thumbs")
	generate_html(photo_list)
