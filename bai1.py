def tao(a, n, m):
    lst =  []
    id = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[id])
            id+=1
        lst.append(row)
    return lst





n = int(input("nhap n: "))
m = int(input("nhap m: "))
k = int(input("nhap k: "))
print("nhap ham a: ")
a = [int(input()) for _ in range(k)]
if n * m > len(a):
    print("khong xay dung dc ma tran")
else : 
    print("co the xay dung dc ma tran")
    ham =  tao(a,n,m)
    print(ham)