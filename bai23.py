# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:37:16 2024

@author: Dell
"""
a = float(input("nhahp so thu nhat: "))
b = float(input("nhap so thu hai: "))
c = float(input("nhap so thu ba: "))
delta= b**2-4*a*c
if a==0:
    ket_qua = -c/b
    print("Ket qua bang: ", ket_qua)
else:
    if delta>0:
        print("Phuong trinh co hai nghiem phan biet")
        x1= (-b+delta**(1/2))/2*a
        x2= (-b-delta**(1/2))/2*a
        print("Nghiem x1= ", x1,",","Nghiem x2=", x2)
    elif delta==0:
        print("Phuong trinh co nghiem kep")
        Nghiem_kep = -b/(2*a)
        print("Ket qua bang: ", Nghiem_kep)
    else:
        print("Phuong trinh vo nghiem")