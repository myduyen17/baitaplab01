# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:56:10 2024

@author: Dell
"""
a = input("Nhập một chữ cái: ")
if a.isupper():
    print("Chữ cái : ", a.lower())
elif a.islower():
    print("Chữ cái : ", a.upper())
else:
    print("Vui lòng nhập lại")


    
