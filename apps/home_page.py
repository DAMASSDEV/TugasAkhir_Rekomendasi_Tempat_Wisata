import streamlit as st
import base64

def home_page():
    st.set_page_config(
        page_title="Sistem Rekomendasi Tempat Wisata",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("SISTEM REKOMENDASI WISATA")
    st.markdown(
        """
        Selamat datang di **Sistem Rekomendasi Wisata**
        Aplikasi ini menggunakan *Forward Chaining* untuk membantu menemukan
        tempat wisata berdasarkan **minat dan kisaran harga** pilihanmu.
        """
    )

    def img_to_base64(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()

    images = {
        "danar": img_to_base64("image/danar.jpg"),
        "alif": img_to_base64("image/alif.jpg"),
        "fuad": img_to_base64("image/fuad.jpg"),
        "rafif": img_to_base64("image/rafif.png"),
        "rifky": img_to_base64("image/rifky.jpg"),
    }

    HTML = f"""
        <style>
            .gallery {{
                display:flex;
                flex-wrap:wrap;
                justify-content:space-around;
                align-items:center;
            }}
            .gallery-item {{
                text-align:center;
                margin:20px;
            }}
            .gallery-item img {{
                width:200px;
                height:200px;
                border-radius:50%;
            }}
            h1 {{
                color:yellow;
                font-size:20px;
            }}
            p {{
                color:white;
            }}
        </style>

        <div class="gallery">
            <div class="gallery-item">
                <img src="data:image/jpeg;base64,{images['danar']}">
                <h1>Danar Mas Saputra</h1>
                <p>50423331</p>
            </div>
            <div class="gallery-item">
                <img src="data:image/jpeg;base64,{images['alif']}">
                <h1>Alif Muhammad Aldaffa</h1>
                <p>50423332</p>
            </div>
            <div class="gallery-item">
                <img src="data:image/jpeg;base64,{images['fuad']}">
                <h1>Ahmad Nur Fuadi</h1>
                <p>50423333</p>
            </div>
            <div class="gallery-item">
                <img src="data:image/png;base64,{images['rafif']}">
                <h1>Muhammad Rafif Falih</h1>
                <p>50423980</p>
            </div>
            <div class="gallery-item">
                <img src="data:image/jpeg;base64,{images['rifky']}">
                <h1>Rifky Putra Dwiandhika</h1>
                <p>51423301</p>
            </div>
        </div>
    """

    st.markdown(HTML, unsafe_allow_html=True)

home_page()
