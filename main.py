import streamlit as st
from apps.home_page import home_page
from apps.main_page import main_page
from apps.dataset import dataset


def main():
    if "page" not in st.session_state:
        st.session_state.page = "home"
    with st.sidebar:
            st.image('./image/main_photo.jpg', caption='Welcome to Rekomendasi Tempat Wisata')
            st.markdown("### 📌 Navigasi")

            if st.button("🏠 Home"):
                st.session_state.page = "home"
            if st.button("🎯 Main Rekomendasi"):
                st.session_state.page = "main_rekomendasi"
            if st.button("♾️ Dataset Wisata di Yogyakarta"):
                st.session_state.page = "dataset"

            st.markdown("---")
            st.caption("@Kelompok Sistem Rekomendasi Forward Chaining")

    if st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "main_rekomendasi":
        main_page()
    elif st.session_state.page == "dataset":
        dataset()



if __name__ == '__main__':
    main()