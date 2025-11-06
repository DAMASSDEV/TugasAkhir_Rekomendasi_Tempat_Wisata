import json
import os

def load_wisata_data():
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(current_dir, 'data', 'wisata.json')

    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        print(f"Error: File {json_path} tidak ditemukan!")
        return []