import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.data_load import load_wisata_data


def dataset():
    st.set_page_config(
        page_title="Dataset Wisata Jogja",
        page_icon="📊",
        layout="wide"
    )

    st.title("📊 Dataset Wisata Yogyakarta")
    st.markdown("Lihat semua data destinasi wisata yang tersedia")
    st.markdown("---")

    wisata_data = load_wisata_data()

    if not wisata_data:
        st.error("❌ Gagal load data!")
        return

    df = pd.DataFrame(wisata_data)

    st.markdown("## 📈 Statistik Dataset")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Destinasi", len(df))

    with col2:
        avg_rating = df['vote_average'].mean()
        st.metric("Rata-rata Rating", f"{avg_rating:.2f}")

    with col3:
        gratis = len(df[(df['htm_weekday'] == 0) & (df['htm_weekend'] == 0)])
        st.metric("Wisata Gratis", gratis)

    with col4:
        kategori_unik = df['kategori'].nunique()
        st.metric("Kategori", kategori_unik)

    st.markdown("---")

    st.markdown("## 🔍 Filter Dataset")
    col_f1, col_f2, col_f3 = st.columns(3)

    with col_f1:
        kategori_filter = st.multiselect(
            "Filter Kategori",
            options=sorted(df['kategori'].unique())
        )

    with col_f2:
        min_rating = st.slider(
            "Rating Minimum",
            min_value=0.0,
            max_value=5.0,
            value=0.0,
            step=0.1
        )

    with col_f3:
        only_gratis = st.checkbox("Hanya Gratis")

    df_filtered = df.copy()

    if kategori_filter:
        df_filtered = df_filtered[df_filtered['kategori'].isin(kategori_filter)]

    df_filtered = df_filtered[df_filtered['vote_average'] >= min_rating]

    if only_gratis:
        df_filtered = df_filtered[(df_filtered['htm_weekday'] == 0) & (df_filtered['htm_weekend'] == 0)]

    st.info(f"Menampilkan {len(df_filtered)} dari {len(df)} destinasi")

    st.markdown("## 📋 Data Wisata")

    df_display = df_filtered.copy()
    df_display['htm_weekday'] = df_display['htm_weekday'].apply(lambda x: f"Rp {x:,}")
    df_display['htm_weekend'] = df_display['htm_weekend'].apply(lambda x: f"Rp {x:,}")

    st.dataframe(
        df_display,
        use_container_width=True,
        height=400
    )

    st.markdown("---")
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Data (CSV)",
        data=csv,
        file_name="wisata_yogyakarta.csv",
        mime="text/csv"
    )


if __name__ == "__main__":
    dataset()