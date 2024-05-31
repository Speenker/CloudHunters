from PIL import Image
import glob
import os
Image.MAX_IMAGE_PIXELS = None

k = 1

files = os.listdir("./data")

#print(files)

for file in files:
    if (file.endswith(".tif")):
        tiff_image = Image.open("data\ ".replace(' ', '') + str(file))
        jpeg_image = tiff_image.convert("RGB")

        save_name = str(k) + ".jpg"

        jpeg_image.save(save_name)
        k += 1

        tiff_image.close()

        #os.close("data\ ".replace(' ', '') + str(file))

        os.replace("data\ ".replace(' ', '') + str(file), "reworked\ ".replace(' ', '') + str(file))


