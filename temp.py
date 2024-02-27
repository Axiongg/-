# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a=float(input("請輸入a的值"))
b=float(input("請輸入b的值"))
c=float(input("請輸入c的值"))
if a!=0:
  r = b**2-4*a*c
  if r>0:
      x1=int((-1*b+r**0.5)/(2*a))
      x2=int((-1*b-r**0.5)/(2*a))
      print("有兩個解 x1=int{x1},x2=int{x2]")
  elif r==0:
      x=input((-1*b+r**0.5)/(2*a))
      print("有一個解 x=(x)")
  else :
      print("沒有實數解")
else :     
  print("沒有實數解")