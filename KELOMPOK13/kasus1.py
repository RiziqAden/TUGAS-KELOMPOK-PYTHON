# kelompok 12
# Anggota Kelompok
# M. Riziq Sirfatullah Alfarizi - i.2211266
# Muhamad  Noufal Falah - i.2210466
# Muhammad  Risyad Fadilah - i.2210148

# kasus 1

# menghitung BOLA
def hitung_keliling_bola(jari_jari):
    return 2 * 3.14 * jari_jari

def hitung_luas_bola(jari_jari):
    return 4 * 3.14 * (jari_jari ** 2)

def hitung_volume_bola(jari_jari):
    return (4/3) * 3.14 * (jari_jari ** 3)

# menghitung KUBUS
def hitung_keliling_kubus(sisi):
    return 12 * sisi

def hitung_luas_kubus(sisi):
    return 6 * (sisi ** 2)

def hitung_volume_kubus(sisi):
    return sisi ** 3

# menghitung BALOK
def hitung_keliling_balok(panjang, lebar, tinggi):
    return 4 * (panjang + lebar + tinggi)

def hitung_luas_balok(panjang, lebar, tinggi):
    return 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

def hitung_volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi


def main():
    print("======================================")
    print("Selamat datang di Aplikasi kelompok 12")
    print("======================================")
    print("Anggota Kelompok")
    print("M. Riziq Sirfatullah Alfarizi - i.2211266")
    print("Muhamad  Noufal Falah - i.2210466")
    print("Muhammad  Risyad Fadilah - i.2210148")

    print("=================")

    while True:
        print("Pilihan:")
        print("a) Bola")
        print("b) Kubus")
        print("c) Balok")
        print("d) Keluar")
        pilihan_utama = input("Masukkan pilihan: ")

        if pilihan_utama == "a":
            print("\nPilihan untuk Bola:")
            print("1. Keliling")
            print("2. Luas")
            print("3. Volume")
            pilihan = int(input("Masukkan pilihan: "))

            if pilihan == 1:
                jari_jari = float(input("Masukkan jari-jari bola: "))
                keliling = hitung_keliling_bola(jari_jari)
                print("Keliling bola:", keliling)
            elif pilihan == 2:
                jari_jari = float(input("Masukkan jari-jari bola: "))
                luas = hitung_luas_bola(jari_jari)
                print("Luas permukaan bola:", luas)
            elif pilihan == 3:
                jari_jari = float(input("Masukkan jari-jari bola: "))
                volume = hitung_volume_bola(jari_jari)
                print("Volume bola:", volume)
            else:
                print("Pilihan tidak valid")

        elif pilihan_utama == "b":
            print("\nPilihan untuk Kubus:")
            print("1. Keliling")
            print("2. Luas")
            print("3. Volume")
            pilihan = int(input("Masukkan pilihan: "))

            if pilihan == 1:
                sisi = float(input("Masukkan panjang sisi kubus: "))
                keliling = hitung_keliling_kubus(sisi)
                print("Keliling kubus:", keliling)
            elif pilihan == 2:
                sisi = float(input("Masukkan panjang sisi kubus: "))
                luas = hitung_luas_kubus(sisi)
                print("Luas permukaan kubus:", luas)
            elif pilihan == 3:
                sisi = float(input("Masukkan panjang sisi kubus: "))
                volume = hitung_volume_kubus(sisi)
                print("Volume kubus:", volume)
            else:
                print("Pilihan tidak valid")

        elif pilihan_utama == "c":
            print("\nPilihan untuk Balok:")
            print("1. Keliling")
            print("2. Luas")
            print("3. Volume")
            pilihan = int(input("Masukkan pilihan: "))

            if pilihan == 1:
                panjang = float(input("Masukkan panjang balok: "))
                lebar = float(input("Masukkan lebar balok: "))
                tinggi = float(input("Masukkan tinggi balok: "))
                keliling = hitung_keliling_balok(panjang, lebar, tinggi)
                print("Keliling balok:", keliling)
            elif pilihan == 2:
                panjang = float(input("Masukkan panjang balok: "))
                lebar = float(input("Masukkan lebar balok: "))
                tinggi = float(input("Masukkan tinggi balok: "))
                luas = hitung_luas_balok(panjang, lebar, tinggi)
                print("Luas permukaan balok:", luas)
            elif pilihan == 3:
                panjang = float(input("Masukkan panjang balok: "))
                lebar = float(input("Masukkan lebar balok: "))
                tinggi = float(input("Masukkan tinggi balok: "))
                volume = hitung_volume_balok(panjang, lebar, tinggi)
                print("Volume balok:", volume)
            else:
                print("Pilihan tidak valid")

        elif pilihan_utama == "d":
            print("Terima kasih! 😁")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
