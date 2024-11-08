from cmath import sqrt


def MAE(n,a):
    sum  = 0
    for i in len(a):
        sum+=abs(a[i][0] - a[i][1])
    sum/= n
    return sum
def MSE(n,a):
    sum  = 0
    for i in len(a):
        sum+= (a[i][0] - a[i][1])**2
    sum/= n
    return sum
def RMSE(n,a): 
    return sqrt(MSE(n,a))
def HuberLoss(n,a,s):
    sum  = 0
    for i in len(a):
        h = abs(a[i][0] - a[i][1])
        if h <= s:
            sum+=h
        else:
            sum+= s * ( h - 0.5 * s)
    sum/= n
    return sum

n = int(input("nhap n: "))
a =  [[int(input()) for _ in range(2)] for _ in range(n) ]
print(a)
