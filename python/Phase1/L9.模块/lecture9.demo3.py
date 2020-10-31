#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
image_file = Image.open("dog.jpeg") # open colour image
logo = Image.open('logo.png') # open logo file
logo.thumbnail((logo.height // 2 ,logo.width // 2))

image_copy = image_file.copy()

#position = (0,0)
position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
image_copy.paste(logo, position) 
image_copy.save('dog_logo.png')

