# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:59:05 2024

@author: Dell
"""
import random
ngay = int(input("ngay sinh cua ban la: "))
thang = int(input("thang sinh cua ban la: "))
nam = int(input("nam sinh cua ban la: "))
#caua
print("sinh nhat cua ban la: ",ngay,"/",thang,"/",nam)
#caub
print("sinh nhat cua ban la: ",ngay,"/",thang,"/",nam%100)
#cauc
print("sinh nhat cua ban la: ",nam,"/",thang,"/",ngay)