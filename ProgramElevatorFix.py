# Program Elevator untuk Gedung 5 Lantai
print("PROGRAM ELEVATOR")
print("Elevator gedung 5 lantai")
# Program mendisplay banyak lantai
print("Kapasitas maksimum elevator adalah 500 kg")
# Program mendisplay berat maksimum

# Berat dalam kg
elevator = 400
b_total = 900

# Program membuat list berat penumpang
# Kamus
# berat : array
# i, orang : integer
# Algoritma
def berat(orang):
    # Fungsi untuk membuat array penumpang
    berat = [0 for i in range(orang)]
    for i in range(orang):
        berat[i] = int(input(f"Masukkan berat orang ke- {i + 1}:"))
    return berat

# Program mencari berat total (berat penumpang + berat elevator)
# Kamus
# berat : array
# i, orang : integer
# Algoritma
def penumpang(orang):
    # Fungsi untuk berat total elevator
    p_total = 0  # berat total penumpang
    elev_total = 0  # berat total elevator diinisiasi bernilai 0
    for i in range(orang):
        p_total += b[i]
    elev_total = p_total + elevator
    return elev_total

# Program memasukkan tujuan lantai penumpang
# Kamus
# lantai : array
# i, orang : integer
# Algoritma
def lantai(orang):
    # Fungsi untuk membuat array tujuan penumpang
    lantai = [0 for i in range(orang)]
    for i in range(orang):
        lantai[i] = int(input(f"Masukkan lantai yang dituju penumpang ke- {i + 1}:"))
        # Asumsi tujuan yang dituju tidak melebihi lantai dalam gedung
    return lantai

# Program cara kerja Elevator
# Kamus
# Algoritma
def kerja(L1, L2):
    # Fungsi untuk membuat array lantai akhir penumpang
    tambah_lantai = 0
    if L1 < L2:
        print("======================================")
        for i in range(L1, L2):
            tambah_lantai += 1
            print(f"Elevator naik ke lantai {L1 + tambah_lantai}")
        print(f"Elevator tiba di lantai {L1 + tambah_lantai}")
        print("======================================")
    elif L1 > L2:
        print("======================================")
        for i in range(L1, L2, -1):
            tambah_lantai += 1
            print(f"Elevator turun ke lantai {L1 - tambah_lantai}")
        print(f"Elevator tiba di lantai {L1 - tambah_lantai}")
        print("======================================")
    else:
        pass
        # asumsi penumpang tidak memencet tombol untuk lantai yang sama

# Proses input menginput
print(" ")
banyak_orang = int(input("Masukkan banyak penumpang yang masuk: "))
b = berat(banyak_orang)
p = penumpang(banyak_orang)
print(" ")
# Lantai awal penumpang
L1 = int(input("Anda di lantai: "))
# asumsi penumpang menginput lantai tidak lebih dari lantai dalam gedung
print("======================================")
print(f"Elevator menuju lantai {L1}")
print(f"Elevator tiba di lantai {L1}")
print("======================================")

# Loop kerja elevator
while banyak_orang != 0:
    # Program mengecek apakah elevator dapat beroperasi
    while p > b_total:
        print("======================================")
        print("Beban melebihi kapasitas elevator")
        # Mengeluarkan orang yang terakhir masuk ke elevator
        p -= b[banyak_orang - 1]
        b.remove(b[banyak_orang-1])
        banyak_orang -= 1
        print(f"Penumpang dalam elevator tersisa {len(b)} orang")
        if banyak_orang == 0:
            print("Elevator berhenti beroperasi")
            break
    else:  # banyak penumpang > 0 & p < b_total
        print(" ")
        l = lantai(banyak_orang)  # array lantai yang dituju
        l = list(set(l))
        print(" ")
        arah=input('Masukkan arah lift (Naik/Turun): ')
        print(" ")
        temp = []
        tempe = []
        total = -1
        if arah=='Naik':
            for i in range(len(l)):
                if l[i]<L1:
                    temp.append(l[i])
                else:
                    tempe.append(l[i])
                    total+=1
            temp=temp[::-1]
        elif arah=='Turun':
            for i in range(len(l)):
                if l[i]>L1:
                    temp.append(l[i])
                else:
                    tempe.append(l[i])
                    total+=1
            tempe=tempe[::-1]

        if len(tempe)==len(l):
            for i in range(len(l)):
                print(f"Anda ingin ke lantai {l[i]}")
                kerja(L1, l[i])
                print(f"Anda di lantai {l[i]}")
                L1 = l[i]
        else:
            for i in range(len(tempe)):
                print(f"Anda ingin ke lantai {tempe[i]}")
                kerja(L1, tempe[i])
                print(f"Anda di lantai {tempe[i]}")
                L1 = tempe[i]
            for i in range(len(temp)):
                print(f"Anda ingin ke lantai {temp[i]}")
                kerja(L1, temp[i])
                print(f"Anda di lantai {temp[i]}")
                L1 = temp[i]
        print(" ")
        banyak_orang = int(input("Masukkan banyak penumpang yang masuk: "))
        if banyak_orang != 0:
            b = berat(banyak_orang)
            p = penumpang(banyak_orang)

print("Elevator berhenti beroperasi")



