import os
import sys
from PIL import Image

# check if the script is run with a command line argument
if len(sys.argv) != 2:
    print("Usage: python script.py <image_filename>")
    sys.exit()

# get the image file name from command line arguments
image_filename = sys.argv[1]

try:
    # open the image
    img = Image.open(image_filename)
except FileNotFoundError:
    print(f"No such file: '{image_filename}'")
    sys.exit()

# get the dimensions of the image
width, height = img.size

# create a new image with the same dimensions that is all white
white_img = Image.new('RGB', (width, height), 'white')

# get the base name of the image file (without the extension)
base_filename = os.path.splitext(image_filename)[0]

# create the new filename
new_filename = f'{base_filename}-white.jpeg'

# save the new image
white_img.save(new_filename)

print(f"White image saved as {new_filename}")
