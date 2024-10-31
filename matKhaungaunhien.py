import random
dsChu = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

dsSo = ['1','2','3','4','5','6','7','8','9','0']

dsKTDB = ['!','@','#','$','%','&','*','(',')','+','=']

print('Chào mừng bạn đến với chương trình tạo mật khẩu ngẫu nhiên!')
slChu = int(input('Nhập số lượng kí tự chữ: '))
slSo = int(input('Nhập số lượng kí tự số: '))
slKTDB = int(input('Nhập số lượng kí tự đặt biệt: '))

matKhau = []

for i in range(slChu):
    matKhau.append(random.choice(dsChu))

for i in range(slSo):
    matKhau.append(random.choice(dsSo))

for i in range(slKTDB):
    matKhau.append(random.choice(dsKTDB))

random.shuffle(matKhau)

password = ''

for kt in matKhau:
    password += kt

print('Mật khẩu của bạn:', password)