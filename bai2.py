import math
print("nhap n: ")
n =  int(input())
dem = 0
for i in range(2,n):
    so =  int(math.sqrt(i))
    if so * so == i:
        dem+=1
        print(i)
print("nhap cac so co uoc le la: ",dem)
