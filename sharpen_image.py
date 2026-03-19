from PIL import Image, ImageFilter
import os

src = r"d:\]portfolio-2\images\IMG_7547.jpg"
dst = r"d:\]portfolio-2\images\IMG_7547_sharp.jpg"

img = Image.open(src)
sharp = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
sharp.save(dst, format='JPEG', quality=95, subsampling=0)
print('Saved', dst, 'size', os.path.getsize(dst))
