while True:
    n = int(input('nhập n = '))
    if n < 2:
        is_check = False
    else:
        is_check = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                is_check = False
                break
        if is_check:
            print(n, 'là số nguyên tố')
        else:
            print(n,' không phải số nguyên tố')
    if n == 0:
        break