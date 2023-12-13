import sys
import os
from PIL import Image

from_folder = sys.argv[1]
to_folder = sys.argv[2]

if not os.path.exists(to_folder):
    os.makedirs(to_folder)

for file in os.listdir(from_folder):
    image = Image.open(f'{from_folder}{file}')
    clean_name = os.path.splitext(file)[0]
    png_file = image.save(f'{to_folder}{clean_name}.png', 'png')