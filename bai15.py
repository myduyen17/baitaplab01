# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:23:16 2024

@author: Dell
"""
a = int(input("nhap gia tri cua a :"))
b = int(input("nhap gia tri cua b :"))
A = (((a+b)/(a**(1/3)+b**(1/3))-(a*b)**(1/3))/(a**(1/3)-b**(1/3))**2)
print("Gia tri cua bieu thuc A la : ", A)


