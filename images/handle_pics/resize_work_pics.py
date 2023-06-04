import argparse
import os

from PIL import Image, UnidentifiedImageError


def resize_photos(job_num, photo_dir, target_res):
	for file_name in os.listdir(os.path.join("../foto_lavori", job_num, photo_dir)):
		try:
			img = Image.open(os.path.join("../foto_lavori", job_num, photo_dir, file_name))
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
		out_file = os.path.join(os.path.join("../foto_lavori", job_num, photo_dir, file_name))
		img.save(out_file)
		print(f"Saved {out_file}")

if __name__ == '__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument('--job_num', required=True)
	argparser.add_argument('--photo_dir', required=True)
	argparser.add_argument('--target_res', default=1600)
	args = argparser.parse_args()

	resize_photos(args.job_num, args.photo_dir, int(args.target_res))
		