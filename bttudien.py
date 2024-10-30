#Viết hàm đưa vào 1 dictionary có các phần tử có giá trị là số nguyên, tìm và trả về key có giá trị lớn nhất//////////////////////////////////////////
# def maxdict(d):
#     maxkey = None
#     maxvl = float('-inf')
#     for key, value in d.items():
#         if value > maxvl:
#             maxvl = value
#             maxkey = key
#     return maxkey
# d = {} 
# n = int(input('input n: '))
# for i in range(n):
#     keys = input('input key: ')
#     values = input('input value: ')
#     d[keys] = int(values)
# print('key max: ',maxdict(d))

#nhập vào 1 danh sách sv bao gồm: mã sv, tên sv, lớp và in ra màn hình. thông tin mỗi sv in trên 1 dòng/////////////////////////////////////////////////////
# ds = []
# n = int(input('nhập số lượng sv: '))
# for i in range(n):
#     sv = {'ma':'','ten':'','lop':''}
#     for j in sv:
#         value = input(f'nhập {j}: ')
#         sv[j] = value
#     ds.append(sv)
# for i in range(n):
#     print('ma: ',ds[i]['ma'],', ten: ',ds[i]['ten'],', lop: ',ds[i]['lop'])

#QUẢN LÝ HÀNG HÓA ////////////////////////////////////////////////////////////////////////////////////////////////
# cuahang = []
# def inputhang(n):
#     for i in range(n):
#         hang = {'tenhang':'','soluong':'','giaban':''}
#         for j in hang:
#             value = input(f'nhập {j}: ')
#             hang[j] = value
#         cuahang.append(hang)

# def seehang():
#     for i in range(len(cuahang)):
#         print('Hàng hóa ',i+1)
#         print('tên hàng: ',cuahang[i]['tenhang'],', số lượng: ',cuahang[i]['soluong'],', giá bán: ',cuahang[i]['giaban'])

# def sumhang():
#     # return sum(int(hang['soluong']) for hang in cuahang)
#     sum = 0
#     for i in range(len(cuahang)):
#         sum += int(cuahang[i]['soluong'])
#     return sum

# def be5():
#     for i in range(len(cuahang)):
#         if int(cuahang[i]['soluong']) <= 5:
#             print('Hàng hóa ',i+1)
#             print('tên hàng: ',cuahang[i]['tenhang'],', số lượng: ',cuahang[i]['soluong'],', giá bán: ',cuahang[i]['giaban'])

# def lon10():
#     for i in range(len(cuahang)):
#         if int(cuahang[i]['soluong']) >= 10:
#             print('Hàng hóa ',i+1)
#             print('tên hàng: ',cuahang[i]['tenhang'],', số lượng: ',cuahang[i]['soluong'],', giá bán: ',cuahang[i]['giaban'])

# if __name__ == '__main__':
#     print('Quản lý cửa hàng tạp hóa: ')
#     print('1. Nhập danh sách hàng: ')
#     print('2. Hiển thị hàng: ')
#     print('3. Tính tổng số lượng hàng hóa của cửa hàng: ')
#     print('4. Hiển thị thông tin các mặt hàng có số lượng bé hơn hoặc bằng 5: ')
#     print('5. Hiển thị thông tin các mặt hàng có số lượng lớn hơn hoặc bằng 10: ')
#     print('* Hãy nhập số bất kỳ không thuộc [1:5] để thoát!!!')
#     n = int(input('* hãy nhập 1 số bất kì từ 1 - 5: '))
#     print('----------------------------------------------------------------------------------------------')
#     while n > 0 and n <= 5:
#         if n == 1:
#             x = int(input('nhập số lượng hàng:'))
#             inputhang(x)
#         elif n == 2:
#             seehang()
#         elif n == 3:
#             print('Tổng số lượng hàng hóa của cửa hàng: ',sumhang())
#         elif n == 4:
#             print('Các mặt hàng có số lượng bé hơn hoặc bằng 5 là: ')
#             be5()
#         elif n == 5:
#             print('Các mặt hàng có số lượng lớn hơn hoặc bằng 10 là: ')
#             lon10()
#         print('----------------------------------------------------------------------------------------------')
#         print('Quản lý cửa hàng tạp hóa: ')
#         print('1. Nhập danh sách hàng: ')
#         print('2. Hiển thị hàng: ')
#         print('3. Tính tổng số lượng hàng hóa của cửa hàng: ')
#         print('4. Hiển thị thông tin các mặt hàng có số lượng bé hơn hoặc bằng 5: ')
#         print('5. Hiển thị thông tin các mặt hàng có số lượng lớn hơn hoặc bằng 10: ')
#         print('* Hãy nhập số bất kỳ không thuộc [1:5] để thoát!!!')
#         n = int(input('* hãy nhập 1 số bất kì từ 1 - 5: '))
#         print('----------------------------------------------------------------------------------------------')

#QUẢN LÝ TUYỂN SINH///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 3. Xây dựng chương trình quản lý tuyền lớp 10 của một trường X như sau:
# - Số báo danh là một chuỗi có độ dài bằng 5
# - Điểm toán và văn là một số thực có giá trị từ 0 đến 10
# Thực hiện các công việc sau:
# + Nhập danh sách thí sinh từ bàn phím
# + In danh sách vừa nhập ra màn hình
# + Hiển thị danh sách thí sinh có tổng điểm > 10
# + Hiển thị DS thí sinh bị điểm liệt ra màn hình (có ít nhất 1 điểm thi 0 điểm)

# ds = []
# def inpuths(n):
#     for i in range(n):
#         hs = {'id':'', 'name':'','toan':'','van':''}
#         for j in hs:
#             value = input(f'nhập { j}: ')
#             hs[j] = value
#         ds.append(hs)

# def see():
#     for i in range(len(ds)):
#         print('số báo danh: ',ds[i]['id'],', tên: ',ds[i]['name'],', toán: ',ds[i]['toan'],', văn: ',ds[i]['van'])

# def diem10():
#     for i in range(len(ds)):
#         if float(ds[i]['toan']) + float(ds[i]['van']) > 10:
#             print('số báo danh: ',ds[i]['id'],', tên: ',ds[i]['name'],', toán: ',ds[i]['toan'],', văn: ',ds[i]['van'])

# def liet():
#     for i in range(len(ds)):
#         if float(ds[i]['toan']) == 0 or float(ds[i]['van']) == 0:
#             print('số báo danh: ',ds[i]['id'],', tên: ',ds[i]['name'],', toán: ',ds[i]['toan'],', văn: ',ds[i]['van'])
        
# print('----------------------------------------------------------------------------------------------')
# print('Quản lý tuyển lớp 10: ')
# print('1. Nhập danh sách thí sinh từ bàn phím: ')
# print('2. In danh sách vừa nhập ra màn hình: ')
# print('3. Hiển thị danh sách thí sinh có tổng điểm > 10: ')
# print('4. Hiển thị DS thí sinh bị điểm liệt ra màn hình (có ít nhất 1 điểm thi 0 điểm): ')
# print('* Hãy nhập số bất kỳ không thuộc [1:4] để thoát!!!')
# n = int(input('* hãy nhập 1 số bất kì từ 1 - 4: '))
# print('----------------------------------------------------------------------------------------------')

# while n > 0 and n <= 4:
#     if n == 1:
#         x = int(input('nhập số lượng học sinh muốn nhập: '))
#         inpuths(x)
#     elif n == 2:
#         print('Danh sách học sinh vừa nhập:')
#         see()
#     elif n == 3:
#         print('Danh sách thí sinh có tổng điểm > 10:')
#         diem10()
#     elif n == 4:
#         print('Danh sách thí sinh bị điểm liệt:')
#         liet()
#     print('----------------------------------------------------------------------------------------------')
#     print('Quản lý tuyển lớp 10: ')
#     print('1. Nhập danh sách thí sinh từ bàn phím: ')
#     print('2. In danh sách vừa nhập ra màn hình: ')
#     print('3. Hiển thị danh sách thí sinh có tổng điểm > 10: ')
#     print('4. Hiển thị DS thí sinh bị điểm liệt ra màn hình (có ít nhất 1 điểm thi 0 điểm): ')
#     print('* Hãy nhập số bất kỳ không thuộc [1:4] để thoát!!!')
#     n = int(input('* hãy nhập 1 số bất kì từ 1 - 4: '))
#     print('----------------------------------------------------------------------------------------------')

# Viết hàm đưa vào 1 dictionary có các phần tử có giá trị là số nguyên, tìm và trả về key có giá trị lớn nhất///////////////////////////
# d = {}
# def maxdict(d):
#     maxkey = None
#     maxvl = float('-inf')
#     for key, value in d.items():
#         if float(value) > float(maxvl):
#             maxvl = value
#             maxkey = key
#     return maxkey

# n = int(input('nhập số lượng: '))
# for i in range(n):
#     keys = input('nhập key: ')
#     values = input('nhập value: ')
#     d[keys] = values
# for i in d:
#     print(i,' = ',d[i])
# print('key có giá trị lớn nhất là: ',maxdict(d))

# Viết hàm đưa vào 1 dictionary có các phần tử có key là chuỗi, tìm và trả về giá trị của key có độ dài lớn nhất////////////////////////////
# def maxstr(d):
#     maxkey = None
#     maxvl = -1
#     for key in d.items():
#         if len(key) > maxvl:
#             maxvl = len(key)
#             maxkey = key
#     return maxkey

# d = {}
# n = int(input('nhập vào số lượng: '))
# for i in range(n):
#     keys = input('nhập key: ')
#     values = input('nhập value: ')
#     d[keys] = values
# for i in d:
#     print(i,': ',d[i])
# print('key có độ dài lớn nhất là: ',maxstr(d))

# Viết hàm có tham số đầu vào là một list L có các phần tử là chuỗi. Hãy tạo ra một dictionary D mã hóa,////////////////////////////////////////
# với mỗi một phần tử trong L được mã hóa thành một con số (theo thứ tự từ 0 tăng dần lên 1 đơn vị).
# Sau đó trả về list đã được mã hóa
# def mahoa(L):
#     D = {}
#     Lmh = []
#     i = 0
#     for item in L:
#         if item not in D:
#             D[item] = i
#             i += 1
#         Lmh.append(D[item])
#     return D, Lmh
# l = list(map(str, input('nhập list: ').split()))
# D, Lmh = mahoa(l)
# print('dict mã hóa: ',D)
# print('List mã hóa: ',Lmh)

# Viết hàm có tham số đầu vào là một dictionary, 
# hãy tạo một dictionary mới hoán đổi giá trị và key của dictionary đầu vào, 
# rồi trả về dicionary mới đó. 
# Nếu sau khi hoán đổi có 2 key trùng nhau (do dictionary đầu vào có 2 giá trị trùng nhau), hàm trả về None

def newdict(l):
    ln = {}
    for key, value in l.items():
        if value in ln:
            return None
        else:
            ln[value] = key
    return ln

l = {}
n = int(input('nhập số lượng: '))
for i in range(n):
    key = input('nhập key: ')
    value = input('nhập value: ')
    l[key] = value
print(l)
print('sau khi đổi giá trị: ',newdict(l))
