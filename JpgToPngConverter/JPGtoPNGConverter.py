import sys
import os
from pathlib import Path

from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

standard_path = f'//{image_folder}'


#if folder not exist then create new one
#dir = os.path.join("/Users/ahemyu/Desktop/pythonprojects", output_folder)
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for filename in os.listdir(image_folder):

    image = Image.open(f'{image_folder}{filename}')
    full_filename = Path(f'{standard_path}/{filename}')
    filename = full_filename.stem
    image.save(f'{output_folder}/{filename}.png', "png")












