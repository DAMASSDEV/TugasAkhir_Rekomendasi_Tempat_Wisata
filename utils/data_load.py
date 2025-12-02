import os
import pandas as pd

def load_wisata_data():

    

    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, '..', 'data', 'dataset-wisata-jogja-sekitar.csv')
    
    try:
        df = pd.read_csv(csv_path, encoding='utf-8')
        
        # Mapping dari tipe ke kategori 
        kategori_map = {
            'Budaya_Dan_Sejarah': 'budaya',
            'Alam': 'alam',
            'Buatan': 'buatan',
            'Wisata_Air': 'air',
            'Pantai': 'pantai',
            'Museum': 'museum',
            'Agrowisata': 'agro'
        }
        
        # Konversi ke list dictionary
        wisata_list = []
        for idx, row in df.iterrows():
            wisata = {
                'nama': row['nama'],
                'type': row['type'],
                'kategori': kategori_map.get(row['type'], 'lainnya'),
                'vote_average': row['vote_average'],
                'vote_count': row['vote_count'],
                'htm_weekday': row['htm_weekday'],
                'htm_weekend': row['htm_weekend'],
                'latitude': row['latitude'],
                'longitude': row['longitude']
            }
            wisata_list.append(wisata)
        
        print(f"✅ Berhasil load {len(wisata_list)} data wisata")
        return wisata_list
        
    except FileNotFoundError:
        print(f"❌ File tidak ditemukan: {csv_path}")
        return []
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return []