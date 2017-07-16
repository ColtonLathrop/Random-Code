from PIL import Image

def get_image(target_img):
    img = Image.open(target_img)
    return img.load()

def get_size(target_img):
    img = Image.open(target_img)
    return img.size
