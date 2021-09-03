
from PIL import Image,ImageOps
from pytesseract import pytesseract

def extracter(file_name):
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = fr"{file_name}"
    img = Image.open(image_path)
    img_gray=ImageOps.grayscale(img)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img_gray)
    text_split=list(text)
    text_split.pop(-1)
    return "".join(text_split)