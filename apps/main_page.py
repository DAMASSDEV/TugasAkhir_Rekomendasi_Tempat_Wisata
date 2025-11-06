import streamlit as st
from utils.logika_forward import forward_chaining
from utils.data_load import load_wisata_data


def main_page():

    st.set_page_config(
        page_title="Sistem Rekomendasi Tempat Wisata",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("Sistem Rekomendasi Tempat Wisata")

    wisata_data = load_wisata_data()


    minat_input = st.text_input(
        "Masukkan minat (pisahkan dengan koma [,] contoh: alam, budaya, kuliner):"
    )

    harga_input = st.selectbox(
        "Pilihlah harga berikut ini:",
        ['', '50.000-90.000', '100.000-190.000', '200.000-290.000', '300.000-390.000', '400.000-490.000', '500.000-590.000'],
    )

    lokasi_input = st.text_input(
        "Masukkan lokasi umum (contoh: Bali, Yogyakarta, dll) :"
    )

    waktu_input = st.radio(
        "Pilihlah waktu terbaik untuk wisata kamu:",
        ["Pagi", "Siang", "Sore", "Malam"]
    )


    tingkat_input = st.radio(
        "Pilihlah tingkat keramaiannya:",
        ["rendah", "sedang", "tinggi" ]
    )

    aktivitas_input = st.multiselect(
        "Masukkan aktifitas yang ingin dilakukan:",
        ['berenang','berselancar','belanja','kuliner', 'jalan-jalan', 'wisata budaya', 'sunrise', 'fotografi', 'wisata sejarah', 'makan malam', 'menikmati pantai', 'edukasi budaya', 'foto', 'mendaki', 'bermain wahana', 'belajar sejarah', 'snorkelingg', 'trekking', 'melihat orangutan', 'bersantai', 'belajar budaya', 'makan', 'makan malam mewah']
    )

    fasilitas_input = st.multiselect(
        "Pilihlah fasilitas yang diinginkan",
        ["kafe", "toilet", "parkir", "warung", "guide", "reservasi", "lift", "penginapan", "kapal", "valet"]

    )


    if st.button("🔍 Dapatkan Rekomendasi dari sistem kami", type="primary"):
        minat_user = [minat.strip().lower() for minat in minat_input.split(',') if minat.strip()]

        hasil = forward_chaining(
            minat_user,
            harga_input.lower(),
            lokasi_input.lower(),
            waktu_input.lower(),
            aktivitas_input,
            tingkat_input.lower(),
            fasilitas_input,
            wisata_data
        )

        if hasil:
            st.success(f"Ditemukan {len(hasil)} rekomendasi wisata:")
            for h in hasil:
                st.markdown(f"""
                            ---
                                \n
                                **{h['nama']}**\n
                                📍 Lokasi: {h['lokasi']} lebih spesifiknya = {h['lokasi_spesifik']}\n
                                🏷️ Kategori: {", ".join(h['kategori'])}\n
                                💰 Harga: {h['harga'].capitalize()}\n
                                🪟 Suasana: {h['suasana']}\n
                                🖼️ Waktu Terbaik: {h['waktu_terbaik']}\n
                                🚀 Aktivitas: {h['aktivitas']}\n
                                🚨 Tingkat Keramaian: {h['tingkat_keramaian']}\n
                                ❤️ Fasilitas: {h['fasilitas']}\n
                                \n
                            """)
            st.balloons()

        else:
            st.warning("Tidak ditemukan wisata yang sesuai minat dan preferensi anda.")