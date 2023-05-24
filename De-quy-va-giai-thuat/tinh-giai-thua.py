def giai_thua(n):
    if n==0:
        return 1
    else:
        return n*giai_thua(n-1)
n = int(input("Nhập n = "))
print("Giai thừa của ",n,"là: ",giai_thua(n))