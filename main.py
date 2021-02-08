from PIL import Image
from pytesseract import image_to_string

print(image_to_string(Image.open('data_source/21-02-05-1.jpeg')))