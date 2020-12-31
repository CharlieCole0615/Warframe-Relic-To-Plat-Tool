import cv2
import pytesseract
import pyscreenshot as ImageGrab

im=ImageGrab.grab(bbox=(400,400,1400,500))
im.save(r'C:\Users\Charlie\Desktop\tesseract_images\imagegrab.png')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from PIL import Image

image = Image.open(r'C:\Users\Charlie\Desktop\tesseract_images\imagegrab.png')

print(pytesseract.image_to_string(r'C:\Users\Charlie\Desktop\tesseract_images\imagegrab.png'))
