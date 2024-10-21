def kandidat():

    calon = {
        1 : {"nama":"Yudhis", "suara" : 0},
        2 : {"nama":"Maman", "suara" : 0},
        3 : {"nama":"Momon", "suara" : 0},
    }

    for no, data in calon.items():
        print(f"{no} {data['nama']}")

    return calon

def voting(calon):
    pemilih = int(input("Masukkan jumlah mahasiswa dalam 1 kelas : "))

    for i in range(1, pemilih + 1):
        print(f"pemilih ke-{i}")
        while True:
            vote = int(input("Masukkan nomor urut kandidat (1/2/3) : "))
            if vote in calon:
                calon[vote]["suara"] += 1
                break
            else:
                print("Tidak ada kandidat degan nomor urut tsb, silahkan masukkan ulang")
                continue

    return calon

def rekapitulasi(calon):
    print("\nRekapitulasi Suara")

    for no, data in calon.items():
        print(f"{no} {data['nama']} : {data['suara']}")

print("Voting ketua kelas")
print("Pilih kandidat favoritmu")
calon = kandidat()
suara_calon = voting(calon)
rekapitulasi(suara_calon)
