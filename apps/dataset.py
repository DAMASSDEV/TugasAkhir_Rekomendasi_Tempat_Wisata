import streamlit as st
from utils.data_load import load_wisata_data
import pandas as pd

def dataset():
    st.set_page_config(
        page_title="Sistem Rekomendasi Tempat Wisata",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("📊 Dataset Tempat Wisata Indonesia")

    data = load_wisata_data()
    if not data:
        st.warning("Tidak ada data untuk ditampilkan.")
        return

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )
