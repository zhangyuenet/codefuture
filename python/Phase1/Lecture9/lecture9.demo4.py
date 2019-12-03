#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
image_file = Image.open("dog.jpeg") # open colour image
image_file = image_file.convert('RGBA')
logo = Image.open('logo.png') # open logo file
logo = logo.convert('RGBA')
logo_newwidth = int(image_file.width / 3)
logo.thumbnail((logo_newwidth, logo.height/logo.width * logo_newwidth))

result_img = Image.new('RGBA', image_file.size, (0,0,0,0))

result_img.paste(image_file, (0,0))

#分离通道
r,g,b,a = logo.split()

#position = (0,0)
position = ((image_file.width - logo.width), (image_file.height - logo.height))
result_img.paste(logo, position, logo)  
# result_img.paste(logo, position, mask=a) 
result_img.save('dog_logo2.png')

