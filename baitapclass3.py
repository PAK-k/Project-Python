class PTB2():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tinhDelta(self):
        delta = float(self.b)**2 - 4*float(self.a)*float(self.c)
        return delta
    
    def tinhNghiem(self, delta):
        if float(self.a) == 0:
            if float(self.b) == 0:
                if float(self.c) == 0:
                    print('phương trình có vô số nghiệm!')
                else:
                    print('phương trình vô nghiệm!')
            else:
                print('phương trình có nghiệm x = ', -(float(self.c)/float(self.b)))
        else:
            if delta == 0:
                print('phương trình có nghiệm kép x = ',-(float(self.b)/2*float(self.a)))
            elif delta < 0:
                print('phương trình vô nghiệm!')
            else:
                x1 = (-float(self.b) + delta)/2*float(self.a)
                x2 = (-float(self.b) - delta)/2*float(self.a)
                print(f'phương trình có 2 nghiệm x1 = {x1} và x2 = {x2}')

def inputt():
    a = input('nhập a = ')
    b = input('nhập b = ')
    c = input('nhập c = ')
    pt = PTB2(a,b,c)
    return pt

def wfile(pt):
    with open('ptb2.txt','w') as file:
        file.write(f'{pt.a}\n')
        file.write(f'{pt.b}\n')
        file.write(f'{pt.c}')

def rfile():
    with open('ptb2.txt') as file:
        a = file.readline()
        b = file.readline()
        c = file.readline()
        pt = PTB2(a,b,c)
        return pt

if __name__ == '__main__':
    while True:
        print('-------------------------------------')
        print('Chương trình có các chức năng sau:')
        print('1. Nhập hệ số của phương trình:')
        print('2. Tính nghiệm:')
        print('3. Đọc hệ số từ file')
        print('4. Lưu hệ số và thoát')
        print('-------------------------------------')
        choice = int(input('Hãy nhập chương trình bạn muốn thực hiện: '))

        if choice == 1:
            pt = inputt()
        elif choice == 2:
            dt = pt.tinhDelta()
            print(pt.tinhNghiem(dt))
        elif choice == 3:
            pt = rfile()
            print('Đã đọc file thành công!')
        elif choice == 4:
            wfile(pt)
            print('Đã lưu vào file và thoát chương trình!')
            break
        else:
            print('Chức năng bạn chọn không tồn tại!')