import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logika_forward import forward_chaining
from utils.data_load import load_wisata_data


def main_page():
    st.set_page_config(
        page_title="Rekomendasi Wisata Jogja",
        page_icon="🗺️",
        layout="wide"
    )

    with st.sidebar:
        st.image("./image/main.jpg")
        st.title("🎯 Sistem Rekomendasi")
        st.markdown("**Metode:** Forward Chaining")
        st.markdown("**Area:** Yogyakarta")
        st.markdown("---")

        with st.expander("ℹ️ Cara Kerja"):
            st.markdown("""
            **Forward Chaining Rules:**
            1. Kategori cocok → +30 poin
            2. Harga sesuai → +25 poin
            3. Rating tinggi → +20 poin
            4. Popularitas → +15 poin
            5. Gratis → +10 poin
            """)

    st.title("🗺️ Sistem Rekomendasi Wisata Yogyakarta")
    st.markdown("Temukan destinasi wisata terbaik dengan Forward Chaining")
    st.markdown("---")

    wisata_data = load_wisata_data()



    st.markdown("## 📝 Input Preferensi Anda")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎯 Kategori Wisata")
        kategori = st.selectbox(
            "Pilih kategori",
            ["", "alam", "budaya", "pantai", "buatan", "museum", "agro", "air"],
            help="Kosongkan untuk semua kategori"
        )

        st.markdown("### 💰 Budget (Harga Tiket)")
        budget_option = st.selectbox(
            "Pilih range budget",
            ["Gratis", "0 - 50.000", "50.000 - 100.000", "100.000 - 200.000",
             "200.000 - 500.000", "> 500.000", "Semua harga"]
        )

    with col2:
        st.markdown("### ⭐ Rating Minimum")
        rating_min = st.slider(
            "Minimal rating",
            min_value=0.0,
            max_value=5.0,
            value=0.0,
            step=0.5
        )

        st.markdown("### 📊 Info Budget")
        if budget_option == "Gratis":
            st.info("🎉 Cari wisata gratis")
            harga_min = 0
            harga_max = 0
        elif budget_option == "0 - 50.000":
            st.info("💵 Budget: Rp 0 - 50.000")
            harga_min = 0
            harga_max = 50000
        elif budget_option == "50.000 - 100.000":
            st.info("💵 Budget: Rp 50.000 - 100.000")
            harga_min = 50000
            harga_max = 100000
        elif budget_option == "100.000 - 200.000":
            st.info("💵 Budget: Rp 100.000 - 200.000")
            harga_min = 100000
            harga_max = 200000
        elif budget_option == "200.000 - 500.000":
            st.info("💵 Budget: Rp 200.000 - 500.000")
            harga_min = 200000
            harga_max = 500000
        elif budget_option == "> 500.000":
            st.info("💵 Budget: > Rp 500.000")
            harga_min = 500000
            harga_max = 999999999
        else:
            st.info("💵 Budget: Semua harga")
            harga_min = 0
            harga_max = 999999999

    st.markdown("---")

    if st.button("🔍 CARI REKOMENDASI", type="primary", use_container_width=True):

        with st.spinner("⏳ Processing dengan Forward Chaining..."):
            hasil = forward_chaining(
                kategori_user=kategori,
                harga_min=harga_min,
                harga_max=harga_max,
                rating_min=rating_min,
                wisata_data=wisata_data
            )

        if hasil:
            st.balloons()
            st.success(f"✨ Ditemukan {len(hasil)} rekomendasi terbaik!")

            st.markdown("---")
            st.markdown("## 🎯 Hasil Rekomendasi")

            # Tampilkan setiap wisata
            for idx, wisata in enumerate(hasil, 1):
                with st.expander(
                    f"**#{idx} {wisata['nama']}** ⭐ {wisata['vote_average']}/5 | 🏆 Skor: {wisata['skor']}",
                    expanded=(idx <= 3)
                ):
                    col_a, col_b = st.columns([2, 1])

                    with col_a:
                        st.markdown("### 📍 Informasi")
                        st.write(f"**Nama:** {wisata['nama']}")
                        st.write(f"**Kategori:** {wisata['kategori'].upper()}")
                        st.write(f"**Tipe:** {wisata['type']}")
                        st.write(f"**Rating:** ⭐ {wisata['vote_average']}/5")
                        st.write(f"**Vote Count:** 👥 {wisata['vote_count']:,} votes")

                        st.markdown("### 💰 Harga Tiket")
                        if wisata['htm_weekday'] == 0 and wisata['htm_weekend'] == 0:
                            st.write("**🎉 GRATIS!**")
                        else:
                            st.write(f"**Weekday:** Rp {wisata['htm_weekday']:,}")
                            st.write(f"**Weekend:** Rp {wisata['htm_weekend']:,}")

                        st.markdown("### 📍 Lokasi")
                        st.write(f"**Latitude:** {wisata['latitude']}")
                        st.write(f"**Longitude:** {wisata['longitude']}")
                        st.markdown(f"[🗺️ Buka di Google Maps](https://www.google.com/maps?q={wisata['latitude']},{wisata['longitude']})")

                    with col_b:
                        st.markdown("### 🏆 Analisis Skor")
                        st.metric("Total Skor", wisata['skor'])

                        st.markdown("**Alasan Direkomendasikan:**")
                        for alasan in wisata['alasan']:
                            st.markdown(f"✅ {alasan}")

                    st.markdown("---")

        else:
            st.warning("😔 Tidak ada wisata yang sesuai kriteria")
            st.info("💡 Coba ubah filter atau pilih 'Semua harga'")


if __name__ == "__main__":
    main_page()