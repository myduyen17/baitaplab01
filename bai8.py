# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:19:40 2024

@author: Dell
"""

can_nang = float(input("Cân nặng của bạn là: "))

chieu_cao = float(input("Chiều cao của bạn là: "))

BMI = can_nang/( chieu_cao* chieu_cao)

if BMI < 18.5 :

    print("Bạn có vẻ gầy còm? BMI =", BMI, "Chịu khó ăn nhiều thêm nhé!")

if (BMI >=18.5) and (BMI < 23) :

    print("Bạn có dáng chuẩn đấy! BMI =", BMI, "Tiếp tục phát huy nhé! :) ")

if BMI >=23 :

    print("Bạn thừa cân rồi! BMI =", BMI, "Phải chịu khó tập thể thao và ăn nhiều hoa quả! :) ")
