s = input()
k = 'hit'
h = 'HIT'
p = '15'
a = False
b = False

for x in range(len(s)):
    # Check for 'hit' or 'HIT'
    if x <= len(s) - 3 and (s[x:x+3] == k or s[x:x+3] == h):
        a = True
    # Check for '15'
    if x <= len(s) - 2 and s[x:x+2] == p:
        b = True

print("xet co chu HIT or hit trong chuoi:", a)
print("xet co chu so 15 trong chuoi:", b)
