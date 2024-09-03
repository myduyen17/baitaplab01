# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:00:54 2024

@author: Dell
"""
N = int(input("nhập số nguyên dương có hai chữ số: "))
if 10 <= N <= 99:
    tong = (N/10) + (N%10)
    print("Tổng các chữ số của N là : ", tong)
