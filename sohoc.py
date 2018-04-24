#!/usr/bin/env python
a = input('Nhap a: ')
b = input('Nhap b: ')
print "-----------------";
print "a=", a
print "b=", b
print "-----------------";
print "Tong hai so: ", a+b
print 'Hieu hai so: ', a-b
print "Tich hai so: ", a*b
if b==0:
	print "Khong the chia cho 0";
else:
	print "Thuong hai so: ",a,"/",b,"=", a/b
	print "Chia lay du: ",a,"%",b,"=", a%b
	
print "So mu: ",a,"^",b,"=",a**b
