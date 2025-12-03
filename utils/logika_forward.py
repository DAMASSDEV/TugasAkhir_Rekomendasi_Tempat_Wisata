def forward_chaining(kategori_user, harga_min, harga_max, rating_min, wisata_data):
    """
    Forward Chaining
    RULES:
    1. IF kategori cocok THEN lanjut, ELSE skip
    2. IF rating >= minimum THEN lanjut, ELSE skip
    3. IF harga sesuai budget THEN lanjut, ELSE skip
    4. IF rating >= 4.5 THEN skor +20
       ELSE IF rating >= 4.0 THEN skor +15
       ELSE IF rating >= 3.5 THEN skor +10
       ELSE skor +5
    5. IF vote_count > 50000 THEN skor +15
       ELSE IF vote_count > 20000 THEN skor +10
       ELSE IF vote_count > 10000 THEN skor +5
       ELSE skor +0
    6. IF gratis THEN skor +10
    """

    hasil = []

    for wisata in wisata_data:
        skor = 0
        alasan = []


        if kategori_user == "":
            skor = skor + 30
            alasan.append("Semua kategori")
        else:
            if kategori_user == wisata['kategori']:
                skor = skor + 30
                alasan.append(f"Kategori {kategori_user}")
            else:
                continue

        rating = wisata['vote_average']

        if rating >= rating_min:
            pass
        else:
            continue


        harga_weekday = wisata['htm_weekday']
        harga_weekend = wisata['htm_weekend']
        harga_rata = (harga_weekday + harga_weekend) / 2

        if harga_min <= harga_rata <= harga_max:
            skor = skor + 25
            alasan.append(f"Harga sesuai (Rp {int(harga_rata):,})")
        else:
            continue


        if rating >= 4.5:
            skor = skor + 20
            alasan.append(f"Rating sangat tinggi ({rating})")
        else:
            if rating >= 4.0:
                skor = skor + 15
                alasan.append(f"Rating tinggi ({rating})")
            else:
                if rating >= 3.5:
                    skor = skor + 10
                    alasan.append(f"Rating bagus ({rating})")
                else:
                    skor = skor + 5
                    alasan.append(f"Rating cukup ({rating})")

        vote_count = wisata['vote_count']

        if vote_count > 50000:
            skor = skor + 15
            alasan.append("Sangat populer (>50k votes)")
        else:
            if vote_count > 20000:
                skor = skor + 10
                alasan.append("Populer (>20k votes)")
            else:
                if vote_count > 10000:
                    skor = skor + 5
                    alasan.append("Cukup populer (>10k votes)")
                else:
                    skor = skor + 0


        if harga_weekday == 0:
            if harga_weekend == 0:
                skor = skor + 10
                alasan.append("🎉 GRATIS!")
            else:
                pass
        else:
            pass

        wisata_copy = wisata.copy()
        wisata_copy['skor'] = skor
        wisata_copy['alasan'] = alasan
        hasil.append(wisata_copy)

    hasil_sorted = sorted(hasil, key=lambda x: x['skor'], reverse=True)

    return hasil_sorted[:10]


def hitung_skor_detail(wisata):

    print(f"\n=== Detail Scoring: {wisata['nama']} ===")
    print(f"Total Skor: {wisata['skor']}")
    print("Breakdown:")
    for i, alasan in enumerate(wisata['alasan'], 1):
        print(f"  {i}. {alasan}")

