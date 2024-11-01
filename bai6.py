import math
def binary(x):
    if x >= 1:
        return 1
    else: 
        return 0
def sigmoid(x):
    return 1 / ( 1 + math.e**(-x))
def ELU(x):
    if x < 0:
        return 0.01 * ( math.e**x - 1)
    else:
        return x
    
n = int(input("nhap n: "))
do = input("nhap kieu tinh: ")
if do == "binary":
    print(f"tinh theo binary: {binary(n)}")
elif do == "sigmoid":
    print(f"tinh theo sigmoid: {sigmoid(n)}")
else:
    print(f"tinh theo ELU: {ELU(n)}")