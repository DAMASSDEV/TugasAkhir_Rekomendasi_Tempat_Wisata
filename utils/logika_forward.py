def forward_chaining(kategori_user, harga_min, harga_max, rating_min, wisata_data):
    """
    Forward Chaining dengan logika IF-ELSE yang mudah dibaca manusia
    
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
    
    # Proses setiap wisata satu per satu
    for wisata in wisata_data:
        skor = 0
        alasan = []
        
        # ==========================================
        # RULE 1: CEK KATEGORI
        # ==========================================
        if kategori_user == "":
            # Jika user tidak pilih kategori, semua kategori diterima
            skor = skor + 30
            alasan.append("Semua kategori")
        else:
            # Jika user pilih kategori tertentu
            if kategori_user == wisata['kategori']:
                # Kategori cocok, lanjut
                skor = skor + 30
                alasan.append(f"Kategori {kategori_user}")
            else:
                # Kategori tidak cocok, skip wisata ini
                continue
        
        # ==========================================
        # RULE 2: CEK RATING MINIMUM
        # ==========================================
        rating = wisata['vote_average']
        
        if rating >= rating_min:
            # Rating memenuhi syarat minimum, lanjut
            pass
        else:
            # Rating di bawah minimum, skip wisata ini
            continue
        
        # ==========================================
        # RULE 3: CEK HARGA SESUAI BUDGET
        # ==========================================
        harga_weekday = wisata['htm_weekday']
        harga_weekend = wisata['htm_weekend']
        harga_rata = (harga_weekday + harga_weekend) / 2
        
        if harga_min <= harga_rata <= harga_max:
            # Harga sesuai budget, lanjut
            skor = skor + 25
            alasan.append(f"Harga sesuai (Rp {int(harga_rata):,})")
        else:
            # Harga di luar budget, skip wisata ini
            continue
        
        # ==========================================
        # RULE 4: SCORING BERDASARKAN RATING
        # ==========================================
        if rating >= 4.5:
            # Rating sangat tinggi
            skor = skor + 20
            alasan.append(f"Rating sangat tinggi ({rating})")
        else:
            if rating >= 4.0:
                # Rating tinggi
                skor = skor + 15
                alasan.append(f"Rating tinggi ({rating})")
            else:
                if rating >= 3.5:
                    # Rating bagus
                    skor = skor + 10
                    alasan.append(f"Rating bagus ({rating})")
                else:
                    # Rating cukup
                    skor = skor + 5
                    alasan.append(f"Rating cukup ({rating})")
        
        # ==========================================
        # RULE 5: SCORING BERDASARKAN POPULARITAS
        # ==========================================
        vote_count = wisata['vote_count']
        
        if vote_count > 50000:
            # Sangat populer
            skor = skor + 15
            alasan.append("Sangat populer (>50k votes)")
        else:
            if vote_count > 20000:
                # Populer
                skor = skor + 10
                alasan.append("Populer (>20k votes)")
            else:
                if vote_count > 10000:
                    # Cukup populer
                    skor = skor + 5
                    alasan.append("Cukup populer (>10k votes)")
                else:
                    # Tidak terlalu populer
                    skor = skor + 0
        
        # ==========================================
        # RULE 6: BONUS JIKA GRATIS
        # ==========================================
        if harga_weekday == 0:
            if harga_weekend == 0:
                # Benar-benar gratis
                skor = skor + 10
                alasan.append("🎉 GRATIS!")
            else:
                # Tidak gratis
                pass
        else:
            # Tidak gratis
            pass
        
        # Simpan hasil dengan skor
        wisata_copy = wisata.copy()
        wisata_copy['skor'] = skor
        wisata_copy['alasan'] = alasan
        hasil.append(wisata_copy)
    
    # Urutkan dari skor tertinggi ke terendah
    hasil_sorted = sorted(hasil, key=lambda x: x['skor'], reverse=True)
    
    # Ambil 10 teratas saja
    return hasil_sorted[:10]


def hitung_skor_detail(wisata):
    """
    Fungsi untuk menjelaskan detail scoring
    """
    print(f"\n=== Detail Scoring: {wisata['nama']} ===")
    print(f"Total Skor: {wisata['skor']}")
    print("Breakdown:")
    for i, alasan in enumerate(wisata['alasan'], 1):
        print(f"  {i}. {alasan}")

