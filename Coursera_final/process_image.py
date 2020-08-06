from PIL import Image
import os
source = "source_tiff"
destination = "destination_tiff"
for file_name in os.listdir(source):
    im = Image.open(f"{source}/{file_name}")
    # print(im.mode)
    if im.mode == 'RGBA':
        im = im.convert('RGB')
    splitted_file_name = file_name.split(".")
    file_name = ''.join(splitted_file_name[:len(splitted_file_name)-1])
    print(file_name)
    dest_file_name = f"{destination}/{file_name}.JPEG"
    im.rotate(90).resize((128,128)).save(dest_file_name,"JPEG")
    # im.save(dest_file_name,"JPEG")
    # print(file_name)

for file_name in os.listdir(destination):
    im = Image.open(f"{destination}/{file_name}")
    print(im.format,im.size)