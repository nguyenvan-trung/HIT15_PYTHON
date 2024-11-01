email = input("nhap email: ")
duoi =  "@gmail.com"

if len(email) < len(duoi) and email[-len(duoi):] == duoi: 
    print("valid")
else:
    print("Invalid")

