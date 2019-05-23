# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:04:53 2019

@author: computer
"""

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("Sample1.jpg","rt")
draw = ImageDraw.Draw(img)

selectFont = ImageFont.truetype("FontName.ttf", size = 60)



draw.text( (x,y), text, (r,g,b), font=selectFont
# (x,y) is the starting position for the draw object
# text is the text to be entered
# (r,g,b) represents the color eg (255,0,0) is Red
# font is used to specify the Font object

img.save( 'certi.pdf', "PDF", resolution=100.0)

