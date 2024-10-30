class SinhVien:
    def __init__(self, hoTen, lop, que, diemTA, diemDA):
        self.hoTen = hoTen
        self.lop = lop
        self.que = que
        self.diemTA = diemTA
        self.diemDA = diemDA
    
    def tinhDTB(self):
        dtb = (self.diemTA + self.diemDA) / 2
        return round(dtb, 2)
    
    def xeploai(self, dtb):
        if dtb < 5:
            print('xếp loại yếu')
        elif 5 <= dtb < 7:
            print('xếp loai trung binh')
        elif 7 <= dtb < 8:
            print('xếp loại khá')
        elif 8 <= dtb < 9:
            print('xếp loại giỏi')
        else:
            print('xếp loại xuất sắc')

def tinhHocBong(dtb):
    if dtb >= 9:
        print('học bổng 5.000.000 đồng')
    else:
        print('không có học bổng')

# dsSV = []

sv1 = SinhVien('Kiệt',' 21CNTT3', 'Quảng Nam', 8, 9)
sv2 = SinhVien('Trường','21CNTT2', 'Quảng Ngãi', 10, 8)

print(sv1.hoTen, sv1.lop, sv1.que, sv1.diemTA, sv1.diemDA, sv1.tinhDTB())
print(sv2.hoTen, sv2.lop, sv2.que, sv2.diemTA, sv2.diemDA, sv2.tinhDTB())

# dsSV.append(sv1)
# dsSV.append(sv2)

# print(dsSV[0].hoTen)

sv1.xeploai(sv1.tinhDTB())
sv2.xeploai(sv2.tinhDTB())

tinhHocBong(sv1.tinhDTB())
tinhHocBong(sv2.tinhDTB())