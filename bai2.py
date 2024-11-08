n = int(input("nhap n: "))
m = int(input("nhap m: "))
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
lst = []
for i in range(max(n,m)):
    if i < n:
        lst.append(a[i])
    if i < m:
        lst.append(b[i])
print(lst)
