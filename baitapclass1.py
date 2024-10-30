# Xây dựng chương trình quản lý môn học gồm các thông tin:
# Mã môn học, tên môn học, số tín chỉ. Chương trình thực hiện được các công việc sau:
# - Nhập được 1 danh sách môn học
# - Hiển thị thông tin các môn học
# - Thêm được một môn học
# - Xoá được một môn học theo mã
# - Tìm kiếm thông tin môn học theo cả 3 trường: Mã môn học, tên môn học và số tín chỉ 
# - Ghi thông tin của các môn học vào tệp MonHoc.txt
# - Đọc thông tin môn học từ tệp MonHoc.txt
import pandas as pd

class MonHoc():
    def __init__(self, maMH, tenMH, soTC):
        self.maMH = maMH
        self.tenMH = tenMH
        self.soTC = soTC
    
    def hienThiMH(self):
        print('mã môn học:',self.maMH)
        print('tên môn học:',self.tenMH)
        print('số tín chỉ:',self.soTC)

# Nhập danh sách môn học
dsMH = []

def inputDSMH():
    n = int(input('nhập số môn học: '))
    for i in range(n):
        maMH = input('nhập mã môn học: ')
        tenMH = input('nhập Tên môn học: ')
        soTC = input('nhập số tín chỉ: ')
        mh = MonHoc(maMH, tenMH, soTC)
        dsMH.append(mh)

# Hiển thị thông tin các môn học
def seeDSMH():
    print('danh sách môn học là:')
    for i in range(len(dsMH)):
        print('thông tin môn học',i+1)
        dsMH[i].hienThiMH()

# Thêm môn học
def addMH():
    print('nhập vào thông tin môn học bạn muốn thêm:')
    maMH = input('nhập mã môn học: ')
    tenMH = input('nhập vào tên môn học: ')
    soTC = input('nhập vào số tín chỉ: ')
    mh = MonHoc(maMH, tenMH, soTC)
    dsMH.append(mh)

# Xóa môn học theo mã
def deleteMH():
    maXoa = input('nhập mã môn học bạn muốn xóa: ')
    for mh in dsMH:
        if (mh.maMH == maXoa):
            dsMH.remove(mh)

# Tìm kiếm 
def search():
    info = input('nhập thông tin muốn tìm kiếm: ')
    ok = 0
    for i in range(len(dsMH)):
        if dsMH[i].maMH == info or dsMH[i].tenMH == info or dsMH[i].soTC == info:
            dsMH[i].hienThiMH()
            ok = 1
    if ok == 0:
        print('không tìm thấy thông tin cần nhập!')

# Ghi thông tin của các môn học vào tệp MonHoc.txt
def wfile():
    with open('Monhoc.txt', 'w') as file:
        for i in range(len(dsMH)):
            file.write(f'{dsMH[i].maMH},')
            file.write(f'{dsMH[i].tenMH},')
            file.write(f'{dsMH[i].soTC}\n')

# - Đọc thông tin môn học từ tệp MonHoc.txt
def rfile():
    df = pd.read_csv('Monhoc.txt', sep = ',', header=None, names=['mã môn học','tên môn học','số tín chỉ'])
    print(df)

if __name__ == '__main__':
    while True:

        print('------------------------------------------------')
        print('Chương trình thực hiện được các công việc sau:')
        print('1. Nhập được 1 danh sách môn học')
        print('2. Hiển thị thông tin các môn học')
        print('3. Thêm được một môn học')
        print('4. Xoá được một môn học theo mã')
        print('5. Tìm kiếm thông tin môn học theo cả 3 trường: Mã môn học, tên môn học và số tín chỉ') 
        print('6. Đọc thông tin môn học từ tệp MonHoc.txt')
        print('7. Lưu và Thoát')
        print('------------------------------------------------')
        n = int(input('Hãy nhập 1-7 để thực hiện chức năng: '))

        if n == 1:
            inputDSMH()
        elif n == 2:
            seeDSMH()
        elif n == 3:
            addMH()
        elif n == 4:
            deleteMH()
        elif n == 5:
            search()
        elif n == 6:
            rfile()
        elif n == 7:
            print('Đã ghi thông tin của các môn học vào tệp MonHoc.txt')
            wfile()
            print('Cảm ơn bạn đã sử dụng chương trình!')
            break