# kelompok 12
# Anggota Kelompok
# M. Riziq Sirfatullah Alfarizi - i.2211266
# Muhamad  Noufal Falah - i.2210466
# Muhammad  Risyad Fadilah - i.2210148

# kasus 4

input = int(input("Enter max data: "))
for i in range(input, 0, -1):
    X = '* ' * i
    print(X.ljust(input))