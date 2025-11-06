def forward_chaining(minat_user, harga_user, lokasi_user, waktu_user, aktivitas_user, tingkat_user, fasilitas_user, wisata_data):

    hasil = []
    cocok_tambahan = False


    for wisata in wisata_data:
        if not any(minat in [wisata.lower() for wisata in wisata['kategori']] for minat in minat_user):
            continue
        if lokasi_user:
            if not (lokasi_user.lower() in wisata['lokasi'].lower()):
                continue
        if harga_user:
            if harga_user not in wisata['harga'].lower():
                continue
        if any(akt in [a.lower() for a in wisata['aktivitas']] for akt in aktivitas_user):
            cocok_tambahan = True
        elif wisata['waktu_terbaik'].lower() == waktu_user:
            cocok_tambahan = True
        elif wisata['tingkat_keramaian'].lower() == tingkat_user:
            cocok_tambahan = True
        elif any(fas in [f.lower() for f in wisata['fasilitas']] for fas in fasilitas_user):
            cocok_tambahan = True

        if cocok_tambahan:
            hasil.append(wisata)


    return hasil
