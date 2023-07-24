import qrcode
import random

inp = input("Input the text, link, etc you want to make QR_Code: ")
img = qrcode.make(inp)

name = str(random.randint(1000, 9999))+".png"
img.save(name)
