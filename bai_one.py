import numpy as np

# Bài 1: In ra phiên bản của NumPy
print("Bài 1: Version của NumPy:", np.__version__)

# Bài 2: Tạo một mảng NumPy
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Bài 2: Mảng arr NumPy:", arr)

# Bài 3: Tạo một mảng 2 chiều
n = int(input("Nhập số hàng (n): "))
m = int(input("Nhập số cột (m): "))
arr = np.ones((n, m), dtype=bool)
print("Bài 3: Mảng cần tạo là:", arr)

# Bài 4: In ra phần tử lẻ trong mảng away
away = [i for i in range(20)]
print("Bài 4: Phần tử lẻ trong mảng away là:")
for i in away:
    if i % 2 != 0:  
        print(i)

# Bài 5: Thay thế phần tử lẻ bằng -1
away = [i for i in range(20)]
print("Bài 5: Mảng sau khi thay lẻ thành -1 là:")
for i in range(len(away)):
    if away[i] % 2 != 0:  
        away[i] = -1
print(away)

# Bài 6: Thay thế phần tử thỏa mãn điều kiện bằng một giá trị khác (thay 1 bằng -10)
away = [i for i in range(20)]
print("Bài 6: Mảng sau khi thay thế 1 thành -10 là:")
for i in range(len(away)):
    if away[i] == 1:  
        away[i] = -10
print(away)

#âu 7: Mảng 2 chiều với 2 hàng
ar = [1, 2, 3, 4, 5, 6]
arr_2d = np.array(ar).reshape(2, 3)
print("Câu 7: Mảng 2 chiều với 2 hàng:")
print(arr_2d)


#câu 8: xếp chồng 2 mảng theo chiều dọc
x = [1, 2, 3]
y = [1, 2, 3]
result = np.vstack((x, y))
print("Câu 8: Xếp chồng 2 mảng theo chiều dọc:")
print(result)

#câu 9 : xếp chồng 2 mảng theo chiều ngang
x = [1, 2, 3]
y = [1, 2, 3]
result = np.hstack((x, y))
print("Câu 9: Xếp chồng 2 mảng theo chiều ngang:")
print(result)

#câu 10: tạo mảng mới lặp lại mỗi phần tử trong arr 3 lần
z = [1, 4, 5]
result = np.repeat(z, 3)
print("Câu 10: Mảng mới lặp lại mỗi phần tử trong arr 3 lần:")
print(result)

#câu 11: Lấy phần tử chung của 2 mảng a và b
a = [14, 463, 13, 79, 0, 2]
b = [14, 4, 62, 2, 6, 2]
common_elements = np.intersect1d(a, b)
print("Câu 11: Phần tử chung của 2 mảng a và b:")
print(common_elements)

#câu 12 : Xoá phần tử từ 1 mảng mà tồn tại trong 1 mảng khác
a = [14, 463, 13, 79, 0, 2]
b = [14, 4, 62, 2, 6, 2]
result = np.setdiff1d(a, b)
print("Câu 12: Mảng a sau khi xoá phần tử tồn tại trong b:")
print(result)

#câu 13:Lấy tất cả vị trí nơi giá trị các phần tử của 2 mảng c,d giống nhau
c = [14, 463, 13, 79, 0, 2]
d = [14, 4, 62, 2, 6, 2]
indices = np.where(np.array(c) == np.array(d))[0]
print("Câu 13: Vị trí nơi các giá trị của 2 mảng giống nhau:")
print(indices)

#câu 14 : Lấy tất cả các giá trị trong 1 phạm vi cho trước từ 1 mảng i < 30 and i > 1
c = [14, 463, 13, 79, 0, 2]
result = np.array(c)[(np.array(c) > 1) & (np.array(c) < 30)]
print("Câu 14: Các giá trị trong phạm vi từ 1 đến 30:")
print(result)

#câu 17: câu 17 :  Hoán 2 hàng trong mảng 2 chiều
h = [[1, 2], [3, 4], [5, 6]]
h[0], h[1] = h[1], h[0]  
print("Câu 17: Mảng sau khi hoán đổi hai hàng:")
print(h)
