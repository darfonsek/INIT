# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:37:49 2020

@author: Darwin Fonseca Lemus
"""

from PIL import Image
import pytesseract
import cv2
import os

print (os.getcwd())

os.chdir("C:/Users/Darwin Fonseca Lemus/Documents/DARWIN/PROYECTO DE VIDA/OCR")

print(pytesseract.image_to_string(Image.open('PRUEBA DE OCR.png')))

print(pytesseract.image_to_string('PRUEBA DE OCR.png'))

## TIF

img = cv2.imread("544.DECLARENTA.TIF")
