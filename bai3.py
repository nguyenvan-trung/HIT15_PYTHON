n =  int(input("nhap n: "))
m = int(input("nhap m: "))

nums1 =  [input("P: ") for _ in range(n)]
nums2 =  [input("S: ") for _ in range(m)]
def tim(a,b):
    lst =  []
    for i in a[::-1]:
        for j in b[::-1]:
            if i == j:
                lst.append(i)
                a.remove(i)
                b.remove(j)
                break
    return lst

print(f'ham la:{tim(nums1, nums2)}')