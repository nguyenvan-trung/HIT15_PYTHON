n = int(input("so luong hoc sinh: "))

for i in range(n):
    print("Nhap ten: ")
    ten = input()
    
    print("nhap diem 1: ")
    x = int(input())
    
    print("nhap diem 2: ")
    y = int(input())
    
    tong_diem = x + y
    if tong_diem < 100:
        xep_loai = "yeu"
    elif 100 <= tong_diem < 150:
        xep_loai = "kha"
    elif 150 <= tong_diem < 190:
        xep_loai = "gioi"
    else:
        xep_loai = "xuat xac"
    
    print(f"{i + 1}: {ten} - Tong diem: {tong_diem} - Xep loai: {xep_loai}")
