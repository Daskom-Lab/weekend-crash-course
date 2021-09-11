import random

passs = ""
garbageNums = 100000
randomPlacement = random.randint(garbageNums / 4, garbageNums * 3 // 4)

answer = "## REDACTED ##"

for x in range(garbageNums):
    if x == randomPlacement:
        asd = answer
    else:
        postcode = str(random.randint(10000, 99999))

        provinsi = random.choice(
            [
                "Jawa Timur",
                "Jawa Barat",
                "Sulawesi",
                "Sumatra Utara",
                "Sumatra Barat",
                "Riau",
                "Jawa Tengah",
                "Kalimantan Barat",
                "Kalimantan Tengah",
                "Kalimantan Selatan",
                "Kalimantan Timur",
                "Daerah Istimewa Yogyakarta",
            ]
        )

        kabkot = f"{random.choice(['Kota', 'Kabupaten'])} {random.choice(['Telkom', 'Baleendah', 'Bandung', 'Bojongsoang', 'Bojongswan', 'Terserah'])}"

        keckel = f"Kecamatan {random.choice(['P304', 'ITU1', 'N109', 'Z404', 'M505', 'X777', 'Z013', 'P313', 'NNNN', 'LMAO'])}"

        if random.randint(0, 1):
            keckel += f" Kelurahan {random.choice(['Apaya', 'Ituituaja', 'Gatau', 'Yaitu', 'Hmmmm', 'Apalah', 'Disana', 'Disitu', 'Disini'])}"

        rt = f"{random.randint(0, 99):02}"
        rw = f"{random.randint(0, 99):02}"
        nomor = str(random.randint(10000, 99999))

        jalan = f"{random.choice(['Jangan', 'Lama', 'Tidak', 'Harus', 'Makin'])}{random.choice(['lama', 'lomo', 'leme', 'lumu', 'limi'])}"

        asd = f"JL. {jalan} No.{nomor}, RT.{rt}/RW.{rw}, {keckel}, {kabkot}, {provinsi} {postcode}"

        if asd == answer:
            continue

    passs += f"{asd}\n"

open("chall.txt", "w").write(passs)
