# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:47:05 2024

@author: Dell
"""
import math
Hình = input("Nhập hình : ")
if Hình == 'vuông':
    a = float(input("Nhập độ dài cạnh : "))
    P = 4 * a
    S = a * a
    print("Chu vi =",P)
    print("Diện tích =",S)
elif Hình == 'chữ nhật':
    b = float(input("Nhập chiều rộng : "))
    a = float(input("Nhập chiều dài : "))
    P = 2 * (a + b)
    S = a * b
    print("Chu vi =",P)
    print("Diện tích =",S)
elif Hình == 'tròn':
    r = float(input("Nhập bán kính : "))
    P = 2 * math.pi * r
    S = math.pi * (r ** 2)
    print("Chu vi =",P)
    print("Diện tích =",S)
else:
    print("Không tìm thấy hình.")

