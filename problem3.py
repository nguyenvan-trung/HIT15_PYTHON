cod = input("nhap chuoi: ")
a  = ""

h = 0
b = ""
c = ""
for i in cod:
    if i <= '9' and i >= '1':
        h =  int(i)
    if i != '[' and i != ']' and i > '9' and i < '1':
        a+=i
    if i == '[' : b = '['
    if i == ']' : b = ']'
    if b == '[' and i != '[': c +=i
    if b == ']':
        for j in range(h-1): a+=c
        c = ""
        b = ""
        h = 0

print(f"day a can tim la:{a}")



