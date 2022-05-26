import pytesseract as pt
import os
import cv2
from PIL import Image


test_image_path = "../test_images/"
create_path = lambda f : os.path.join(test_image_path, f)

test_image_file = os.listdir(test_image_path)

def show_image(image_path, size=(500, 500)):
    image = cv2.imread(image_path)
    image = cv2.resize(image, size)

    cv2.imshow("IMAGE", image)
    cv2.waitkey(0)
    cv2.destroyAllWindow()

pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

available_languages = pt.get_languages(config='')

