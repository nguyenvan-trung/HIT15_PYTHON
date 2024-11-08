n = int(input("Nhập n: "))
k = int(input("Nhập k: "))
a = [int(input(f"Nhập P{i + 1}: ")) for i in range(n)]
a.sort()

l = 0
r = n - 1

while l <= r:
    mid = (l + r) // 2  
    if a[mid] < k:
        l = mid + 1
    else:
        r = mid - 1  

if l < n and a[l] == k:
    print(f'Vị trí là {l} có giá trị {a[l]}')
else:
    print('Không tìm được')
