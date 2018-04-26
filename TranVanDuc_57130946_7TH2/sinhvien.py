#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SinhVien:
	'Đây là phần mô tả về class' 
	def __init__(self,ten="",namSinh=0,khoa=0):
		self.ten=ten
		self.namSinh=namSinh
		self.khoa=khoa
	def get_ten(self):
		return self.ten
	def get_namSinh(self):
		return self.namSinh
	def get_khoa(self):
		return self.khoa
	def set_ten(self):
		ten=input('Nhập tên của sinh viên: ')
		self.ten=ten
	def set_namSinh(self):
		namSinh=input('Nhập năm sinh của sinh viên: ')
		self.namSinh=namSinh
	def set_khoa(self):
		khoa=input('Nhập khóa học của sinh viên: ')
		self.khoa=khoa 
	def toString(self):
		print (self.get_ten(),'-',self.get_namSinh(),'-',self.get_khoa())

