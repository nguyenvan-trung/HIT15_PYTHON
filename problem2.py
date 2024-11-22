chu = str(input("nhap chu: "))
lst = set() 
for i in chu:
    b = 0
    for j in chu:
        if j == i:
            b+=1
    lst.add((i, b))
print(f'day la:{lst}')
