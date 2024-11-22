def tim(x, n):
    sum = 0
    k = 1
    for i in range(n+1):
        if i != 0:
            k *= (x / i)
        sum+=k
    return sum
x = int(input("nhap x: "))
n =  1000000
print(f"gia tri cua e**x : {tim(x,n)}")