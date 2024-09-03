# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:40:28 2024

@author: Dell
"""
#caua
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b
print("Các số theo thứ tự tăng dần là: ", a,">",b,">",c)
#caub
A = int(input("Nhập số nguyên A: "))
if A > 0 :
    A = str(A)
A = ''.join(sorted(A))
A = int(A)
print("Số theo thứ tự tăng dần là :",A)
if A < 0 :
    print("Số nhập vào phải là số nguyên ")

