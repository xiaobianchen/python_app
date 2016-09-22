#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenxiaobian'
#图片处理

import sys
from PIL import Image
img = Image.open('/Users/chenxiaobian/Downloads/863334_100.jpg')
print(img.format,img.size,img.mode)
img.thumbnail((200,100))
img.save('thumb.jpg','JPEG')

pt = sys.path
print(pt)

