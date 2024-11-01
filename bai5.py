n =  int(input("so luong kg ma loai thu i can: "))
sum = 0
li = []
r = 4
inr = -1
l = 101
inl =  -1
for i in range(n):
    x = int(input())
    li.append(x)
    if 5 <=  x <= 100:
        if r <= x: 
            r = x
            inr = i
        if l >= x: 
            l = x
            inl = i

for i in range(n):
    if li[i] < 5:
        print(f"loai {i+1}: an it")
    elif li[i] > 100:
        print(f"loai {i+1}: an nhieu")
    else:
        sum += li[i]
        print(f"loai {i+1}: an trung binh")
print(f"tong thuc an cho cac loai dc tinh la : {sum}")
print(f"loai co suc an nho nhat la:{inl} an {l}")
print(f"loai co suc an lon nhat la:{inr} an {r}")