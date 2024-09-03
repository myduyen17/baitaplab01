# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:05:17 2024

@author: Dell
"""
a = int(input("nhập giờ A :"))
b = int(input("nhập phút A :"))
c = int(input("nhập giây A :"))
A = a*3600+b*60+c
print("A = ",A,"s")
d = int(input("nhập giờ B :"))
e = int(input("nhập phút B :"))
f = int(input("nhập giây B :"))
B = d*3600+e*60+f
print("B = ",B,"s")
C1 = (A + B) 
print("C1 = ",C1,"s")
print("Tổng của hai giờ là :",C1//3600,"giờ",C1%3600//60,"phút",C1%60,"giây")
C2 = A - B
if A < B:
    C2 = B - A
print("C2 = ",C2,"s")
print("Hiệu của hai giờ là :",C2//3600,"giờ",C2%3600//60,"phút",C2%60,"giây")

