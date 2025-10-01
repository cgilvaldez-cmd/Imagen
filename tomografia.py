# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 20:50:27 2025

@author: Carlos Gil
"""
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image_path='tomografia.jpg'
img = mpimg.imread(image_path)
print(type(img))
print(img.shape)

img[80:100, 80:100, :]

plt.imshow(img)
plt.show()