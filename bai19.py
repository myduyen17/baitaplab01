# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:26:27 2024

@author: Dell
"""
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
d = int(input("Nhập số nguyên thứ tư: "))
S = a
if b < S:
    S = b
if c < S:
    S = c
if d < S:
    S = d  
print("Số nhỏ nhất là: ",S)
