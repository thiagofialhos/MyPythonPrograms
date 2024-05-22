#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 19:10:11 2024

@author: thiagofialhos
"""

import os
import sys
folder = '/media/thiagofialhos/BKP/images/Vanessa Chaves'
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.jpg.!qB', '.jpg')
    output = os.rename(infilename, newname)