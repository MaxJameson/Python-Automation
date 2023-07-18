from PIL import Image, ImageEnhance, ImageFilter
import os

# storage image source and save paths
path = './imgs'
pathOut = '/edited'

# loops through images in a file
for filename in os.listdir(path):

    # opens current image
    img = Image.open(f"{path}/{filename}")

    # applies a sharpening filter
    edit = img.filter(ImageFilter.SHARPEN)

    # applies contrast to the image
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    # gets new name for image
    clean_name = os.path.splitext(filename)[0]

    # saves image in edited folder
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')