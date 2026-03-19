from PIL import Image
import pillow_heif
import os

src = r"d:\]portfolio-2\images\IMG_7547.HEIC"
dst = r"d:\]portfolio-2\images\IMG_7547.jpg"

img = pillow_heif.read_heif(src)
image = Image.frombytes(mode=img.mode, size=img.size, data=img.data, decoder_name='raw')
image.save(dst, format='JPEG', quality=100, subsampling=0)
print('Saved', dst, 'size', os.path.getsize(dst))
