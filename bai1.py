sum = 1
print("nhap x: ")
x = int(input())
print("nhap n: ")
n =  int(input())
ans = 1
for i in range(x * 10):
    if i > 0:
        ans*= x/i
        sum+=ans
print("gia tri cua e ^ x:",sum)
ans = 1
sum = 0
for i in range(n+1):
    if i > 0:
        ans/=i
        sum+=ans
print("gia tri cua S la: ", sum)