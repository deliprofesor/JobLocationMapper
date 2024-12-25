import pandas as pd
import folium
from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster

# Veri kümesini yükleyin
file_path = 'job_dataset.csv'  # Dosya yolunu doğru şekilde belirtin
job_data = pd.read_csv(file_path)

# 'job_location' sütununu temizleme
job_data['job_location_cleaned'] = job_data['job_location'].str.replace(r'\+.*location', '', regex=True)
job_data['job_location_cleaned'] = job_data['job_location_cleaned'].str.replace(r'(Remote in |Temporarily Remote in )', '', regex=True)

# Geçerli olmayan değerleri kontrol etme ve düzenleme
invalid_locations = job_data[job_data['job_location_cleaned'].isnull() | ~job_data['job_location_cleaned'].str.contains(',')]
print("Geçerli olmayan satırlar:")
print(invalid_locations)

# Geçerli olmayan satırları kaldırma
job_data = job_data.dropna(subset=['job_location_cleaned'])  # Null değerleri kaldırma
job_data = job_data[job_data['job_location_cleaned'].str.contains(',')]  # Virgül içermeyen satırları kaldırma

# Şehir ve eyalet bilgilerini ayrıştırma
split_location = job_data['job_location_cleaned'].str.split(',', n=1, expand=True)

# Şehir ve eyalet sütunlarını ekleme
job_data['city'] = split_location[0].str.strip()
job_data['state'] = split_location[1].str.strip()

# Meslek kategorisini belirleme ve renk atama
job_data['job_category'] = job_data['job_title'].apply(lambda x: 'Software' if 'developer' in x.lower() else 
                                                      ('Marketing' if 'marketing' in x.lower() else 'Design'))

# Meslek kategorisine göre renkler
category_colors = {
    'Software': 'blue',
    'Marketing': 'green',
    'Design': 'red'
}

# Harita görselleştirmesi oluşturma (Hindistan merkezli)
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5, control_scale=True)

# Geolocator'ı başlatma
geolocator = Nominatim(user_agent="job_locator")

# Marker Cluster ekleme
marker_cluster = MarkerCluster().add_to(india_map)

# Koordinatları önbelleğe alma
location_cache = {}

# Haritaya iş ilanı konumlarını ekleme
for index, row in job_data.iterrows():
    location = f"{row['city']}, {row['state']}"
    
    if location not in location_cache:
        # Konumun coğrafi koordinatlarını almak için geolocator kullanma
        location_info = geolocator.geocode(location)
        location_cache[location] = location_info  # Önbelleğe alma
    else:
        location_info = location_cache[location]
    
    if location_info:
        lat, lon = location_info.latitude, location_info.longitude
        # Meslek kategorisine göre renk atama
        marker_color = category_colors.get(row['job_category'], 'gray')  # Varsayılan renk 'gray'
        
        # Marker ile detaylı bilgi ekleme
        folium.Marker(
            location=[lat, lon],
            popup=f"{location}: {row['job_title']}<br><strong>Category:</strong> {row['job_category']}",
            icon=folium.Icon(color=marker_color, icon="info-sign")
        ).add_to(marker_cluster)

# Harita tipini değiştirme (Satelite harita örneği)
folium.TileLayer('cartodb positron').add_to(india_map)

# Haritayı kaydetme
india_map.save("india_job_location_map_with_categories_clustered.html")
print("Harita oluşturuldu ve 'india_job_location_map_with_categories_clustered.html' olarak kaydedildi.")
