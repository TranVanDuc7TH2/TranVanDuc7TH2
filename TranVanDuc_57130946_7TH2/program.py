#!/usr/bin/python3
from sinhvien import *

sv1=SinhVien()

sv1.set_ten()
sv1.set_namSinh()
sv1.set_khoa() 

print ('----THÔNG TIN SINH VIÊN----')
print ('Tên-Năm sinh-Khóa')
sv1.toString()

