def dichuyen(n, batdau, ketthuc, giua):
    if n == 1:
        print("Chuyển dĩa 1 từ", batdau, "đến", ketthuc)
    else:
        dichuyen(n-1, batdau, giua, ketthuc)
        print("Chuyển dĩa", n, "từ", batdau, "đến", ketthuc)
        dichuyen(n-1, giua, ketthuc, batdau)

n = int(input("Nhập vào số đĩa: "))
dichuyen(n, 'A', 'C', 'B')