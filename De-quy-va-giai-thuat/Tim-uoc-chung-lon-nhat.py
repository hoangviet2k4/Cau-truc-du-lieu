def ucln(a, b):
    if a==0 or b==0:
        return a+b
    while a!=b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a
a = abs(int(input("Nhập số nguyên dương a = ")))
b = abs(int(input("Nhập số nguyên dương b = ")))
print("Ước số chung lớn nhất của", a, "và", b, "là:", ucln(a,b))

