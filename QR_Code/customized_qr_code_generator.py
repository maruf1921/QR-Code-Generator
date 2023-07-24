import qrcode
import random
from PIL import Image

inp = input("Input the text, link, etc you want to make QR_Code: ")
box_size = int(input("Enter the box_size(like 10) :"))
border = int(input("Enter the border_size(like 10) :"))
fill_color = (input("Enter the box_size(like green) :"))
back_color = (input("Enter the box_size(like blue) :"))


qr = qrcode.QRCode(version=1,
                  error_correction = qrcode.constants.ERROR_CORRECT_H,
                  box_size = box_size,
                  border = border)


qr.add_data(inp)
qr.make(fit=True)

img = qr.make_image(fill_color = fill_color, back_color = back_color)

name = str(random.randint(1000, 9999))+".png"
img.save(name)
