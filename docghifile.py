# nhập vào danh sách mã, tên, lớp, quê quán, sau đó lưu thông tin vào 1 file text,
# cuối cùng đọc những thông tin ra màn hình

# n = int(input('nhập số lượng sinh viên muốn nhập vào: '))
# for i in range(n):
#     with open('sinhvien.txt', 'a') as file:
#         ma = input('nhập mã: ') + (' ')
#         ten = input('nhập tên: ') + (' ')
#         lop = input('nhập lớp: ') + (' ')
#         que = input('nhập quên quán: ') + ('\n')
#         file.writelines([ma, ten, lop, que])
with open('sinhvien.txt') as file:
    for sv in file.readlines():
        print(sv, end = '')
    