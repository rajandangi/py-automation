import os
import img2pdf

with open("out.pdf", "wb") as file:
    file.write(img2pdf.convert([i for i in os.listdir(
        'Path of image_Directory') if i.endswith(".jpg")]))
