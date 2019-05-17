# -*- coding: utf-8 -*-
"""
Created on Thu May 16 23:51:30 2019

@author: computer
"""

from PIL import Image
import requests
from io import BytesIO

url = "http://forsk.in/images/Forsk_logo_bw.png"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.save("forsk-logo.png")


# Alternate Solution
"""
import requests

url = "http://forsk.in/images/Forsk_logo_bw.png"
response = requests.get(url)
with open("forsk-logo.png","wb") as f:
    f.write(response.content)
"""