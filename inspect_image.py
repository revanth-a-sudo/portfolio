from PIL import Image
import os

path = r"d:\]portfolio-2\images\IMG_7547.jpg"
img = Image.open(path)
print('format', img.format, 'size', img.size, 'mode', img.mode)
print('file size', os.path.getsize(path))
