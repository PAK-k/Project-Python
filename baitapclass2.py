class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def Shcn(self):
        s = float(self.width) * float(self.height)
        return s
    
    def CVhcn(self):
        cv = (float(self.width) + float(self.height)) * 2
        return cv

def inputhcn():
    print('nhập kích thước hình chữ nhật')
    width = input('nhập chiều rộng hình chữ nhật: ')
    height = input('nhập chiều dài hình chữ nhật: ')
    hcn = Rectangle(width, height)
    return hcn

def wfile(hcn):
    with open('hinhchunhat.txt', 'w') as file:
        file.write(f'{str(hcn.width)},')
        file.write(f'{str(hcn.height)}')
        print('lưu hình chữ nhật vào file thành công!')

def wfilepro(hcn):
    with open('hinhchunhatpro.txt', 'w') as file:
        file.write(f'{str(hcn.width)},')
        file.write(f'{str(hcn.height)},')
        cv = hcn.CVhcn()
        s = hcn.Shcn()
        file.write(f'{str(cv)},')
        file.write(f'{str(s)}')
        print('lưu hình chữ nhật vào file thành công!')

def rfile():
    with open('hinhchunhat.txt') as file:
        s = file.readline()
        width, height = map(float, s.split(','))
        print('chiều rộng: ',width)
        print('chiều dài: ',height)

def rfilepro():
    with open('hinhchunhatpro.txt') as file:
        s = file.readline()
        width, height, cv, s = map(float, s.split(','))
        print('chiều rộng: ',width)
        print('chiều dài: ',height)
        print('chu vi: ',cv)
        print('diện tích: ',s)

if __name__ == '__main__':
    while True:
        print('Chương trình có các chức năng sau:')
        print('1. Nhập kích thước hình chữ nhật: ')
        print('2. Đọc chiều dài và chiều rộng từ file:')
        print('3. Tính chu vi hình chũ nhật:')
        print('4. Tính diện tích hình chữ nhật:')
        print('5. Xem kết quả lần nhập trước:')
        print('6. Lưu kết quả và thoát:')
        print('---------------------------------')
        choice = int(input('nhập chức năng muốn thực hiện: '))

        if choice == 1:
            hcn = inputhcn()
            wfile(hcn)
        elif choice == 2:
            rfile()
        elif choice == 3:
            print('chu vi hình chữ nhật: ', hcn.CVhcn())
        elif choice == 4:
            print('diện tích hình chữ nhật: ', hcn.Shcn())
        elif choice == 5:
            rfilepro()
        elif choice == 6:
            wfilepro(hcn)
            break