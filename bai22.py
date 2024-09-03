# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:33:26 2024

@author: Dell
"""
a = float(input("nhập biến a: "))
b = float(input("nhập biến b: "))
if a==0 and b==0:
    print("Phương trình vô số nghiệm.")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm.")
elif a!=0 and b==0:
    print("Phương trình có nghiệm x=1")
else: 
    x = -b/a
    print("Phương trình có nghiệm x= ",x)
