import numbers
a = int(input())
i = 0
while a != 0:
    b = a % 8
    a = (a - b) / 8
    i+=1
print(i)
d= float(input())
if isinstance(d, numbers.Number):
    print("Danh sach:")
    print(dir(d))
else:
    print("gia tri nhap vao khong kieu so")