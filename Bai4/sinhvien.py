from khoa import Khoa

class SinhVien:
	def __init__(self,MSSV,hoTen,maKhoa):
		self.MSSV = MSSV
		self.hoTen = hoTen 		
		self.maKhoa = maKhoa 
		
	def hienThi(self):
		print ("MSSV: ", self.MSSV)
		print ("Ho Ten: ",self.hoTen)
		print ("Khoa : ",self.maKhoa)

