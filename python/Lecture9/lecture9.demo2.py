#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
image_file = Image.open("dog.jpeg") # open colour image
image_file = image_file.convert('1') # convert image to black and white
image_file.save('dog_black.png')

image_file = image_file.rotate(90)
w, h = image_file.size
image_file.thumbnail((w // 2, h // 2))
image_file.save('dog_2.png')
