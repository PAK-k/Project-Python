import webbrowser
class BaiHat:
    def __init__(self, tenbaihat, url):
        self.tenbaihat = tenbaihat
        self.url = url

class PlayList:
    def __init__(self, tenPlayList, moTa, danhGia, dsBaiHat):
        self.tenPlayList = tenPlayList
        self.moTa = moTa
        self.danhGia = danhGia
        self.dsBaiHat = dsBaiHat

# Hàm nhập bài hát 
def nhapbaihat():
    tenbaihat = input('Nhập tên bài hát: ') + '\n'
    url = input('nhập url bài hát: ') + '\n'
    baiHat = BaiHat(tenbaihat, url)
    return baiHat

# Hàm nhập danh sách bài hát
def nhapdsbaihat():
    dsbaihat = []
    n = int(input('nhập số lượng bài hát: '))
    for i in range(n):
        print('nhập bài hát thứ ',i+1,':')
        baihat = nhapbaihat()
        dsbaihat.append(baihat)
    return dsbaihat

# Hàm nhập PlayList
def nhapPlayList():
    tenPlayList = input('nhập tên PlayList: ') + '\n'
    moTa = input('Nhập mô tả: ') + '\n'
    danhGia = input('nhập đánh giá: ') + '\n'
    dsBaiHat = nhapdsbaihat()
    playList = PlayList(tenPlayList,moTa,danhGia,dsBaiHat)
    return playList

# hàm ghi bài hát vào file
def ghibaihatvaofile(baiHat,file):
    file.write(baiHat.tenbaihat)
    file.write(baiHat.url)

# hàm ghi danh sách bài hát vào file
def ghidsbaihatvaofile(dsbaihat, file):
    n = len(dsbaihat)
    file.write(str(n)+'\n')
    for i in range(n):
        ghibaihatvaofile(dsbaihat[i], file)

# Hàm ghi playlist vào file
def ghiPlayListVaoFile(playList):
    with open('baihat.txt','w') as file:
        file.write(playList.tenPlayList)
        file.write(playList.moTa)
        file.write(playList.danhGia)
        ghidsbaihatvaofile(playList.dsBaiHat, file)

# hàm đọc bài hát từ file
def docbaihattufile(file):
    tenbaihat = file.readline()
    url = file.readline()
    baiHat = BaiHat(tenbaihat, url)
    return baiHat

# hàm đọc danh sách bài hát từ file
def docdsbaihattufile(file):
    dsbaihat = []
    n = int(file.readline())
    for i in range(n):
        baihat = docbaihattufile(file)
        dsbaihat.append(baihat)
    return dsbaihat
    
# Hàm đọc playlist từ file
def docPlayListTuFile():
    with open('baihat.txt') as file:
        tenPlayList = file.readline()
        moTa = file.readline()
        danhGia = file.readline()
        dsBaiHat = docdsbaihattufile(file)
        playList = PlayList(tenPlayList, moTa, danhGia, dsBaiHat)
    return playList

# Hàm in bài hát
def inbaihat(baiHat):
    print('tên bài hát là:',baiHat.tenbaihat,end = '')
    print('url của bài hát là:',baiHat.url,end = '')

# Hàm in danh sách bài hát
def indsbaihat(dsbaihat):
    n = len(dsbaihat)
    print('Thông tin các bài hát:')
    for i in range(n):
        print('bài hát thứ ',i+1,':')
        inbaihat(dsbaihat[i])

# Hàm in PlayList
def inPlayList(playList):
    print('\nThông tin PlayList:')
    print('Tên PlayList là: ',playList.tenPlayList,end='')
    print('Mô tả: ',playList.moTa,end='')
    print('Đánh giá: ',playList.danhGia,end='')
    indsbaihat(playList.dsBaiHat)

# Hàm thêm bài hát vào PlayList
def themBHVaoPlayList(playList):
    tenbaihat = input('nhập tên bài bát muốn thêm: ') + '\n'
    url = input('nhập url của bài hát: ') + '\n'
    baihat = BaiHat(tenbaihat, url)
    playList.dsBaiHat.append(baihat)
    return playList

# Hàm cập nhật thông tin playList
def capNhatTTPlayList(playList):
    print('1. Cập nhật tên PlayList: ')
    print('2. Cập nhật mô tả PlayList: ')
    print('3. Cập nhật đánh giá PlayList: ')
    choice = int(input('Mời bạn chọn (1-3) để cập mong muốn: '))
    if choice == 1:
        tenPlayList = input('Nhập lại tên PlayList: ') + '\n'
        playList.tenPlayList = tenPlayList
    elif choice == 2:
        moTa = input('Nhập lại mô tả mới: ') + '\n'
        playList.moTa = moTa
    else:
        danhGia = input('Nhập lại đánh giá mới: ') + '\n'
        playList.danhGia = danhGia
    return playList

# Hàm xóa một bài hát
def xoaBH(playList):
    indsbaihat(playList.dsBaiHat)
    slBaiHat = len(playList.dsBaiHat)
    bhMuonXoa = int(input(f'Chọn bài hát muốn xóa (1-{slBaiHat}): '))
    for i in range(slBaiHat+1):
        if bhMuonXoa == i:
            del playList.dsBaiHat[bhMuonXoa-1]
    return playList

# Hàm mở một bài hát
def openBH(playList):
    indsbaihat(playList.dsBaiHat)
    slBaiHat = len(playList.dsBaiHat)
    bhMuonMo = int(input(f'Chọn bài hát muốn mở (1-{slBaiHat}): '))
    webbrowser.open(playList.dsBaiHat[bhMuonMo-1].url)

def main():
    # bh = nhapbaihat()
    # ghibaihatvaofile(bh)
    # bh = docbaihattufile()
    # inbaihat(bh)

    # dsbaihat = nhapdsbaihat()
    # ghidsbaihatvaofile(dsbaihat)
    # dsbaihat = docdsbaihattufile()
    # indsbaihat(dsbaihat)

    # playList = nhapPlayList()
    # ghiPlayListVaoFile(playList)
    # playList = docPlayListTuFile()
    # inPlayList(playList)

    try:
        playList = docPlayListTuFile()
    except:
        playList = []
        print('\n Bạn sử dụng chương trình đầu tiên, mời bạn tạo một PlayList mới!')
    while True:

        print('\nChương trình có các chức năng sau:')
        print('1. Tạo một PlayList:')
        print('2. Hiển thị PlayList:')
        print('3. Mở một bài hát:')
        print('4. Thêm một bài hát vào PlayList:')
        print('5. Cập nhật lại thông tin của PlayList:')
        print('6. Xóa một bài hát:')
        print('7. Lưu và thoát:')
        print('------------------------------------')
        luachon = int(input('Vui lòng chọn chức năng mong muốn: '))

        if luachon == 1:
            print('Tạo một PlayList:')
            playList = nhapPlayList()
            input('\nNhấn enter để tiếp tục!')
        elif luachon == 2:
            print('Hiển thị PlayList:')
            inPlayList(playList)
            input('\nNhấn enter để tiếp tục!')
        elif luachon == 3:
            playList = openBH(playList)
            input('\nNhấn enter để tiếp tục!')
        elif luachon == 4:
            playList = themBHVaoPlayList(playList)
            input('\nNhấn enter để tiếp tục!')
        elif luachon == 5:
            playList = capNhatTTPlayList(playList)
            input('\nNhấn enter để tiếp tục!')
        elif luachon == 6:
            playList = xoaBH(playList)
            input('\nNhấn enter để tiếp tục!')
        elif luachon == 7:
            ghiPlayListVaoFile(playList)
            break

main()