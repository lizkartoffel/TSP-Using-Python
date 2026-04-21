import sqlite3

def init_db():
    conn = sqlite3.connect('backend/cities.db')
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS cities')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    lat REAL NOT NULL,
    lon REAL NOT NULL)''') # lat stands for latitude and lon stands for longitude


    conn.commit()   

    
    cursor.execute('SELECT COUNT(*) FROM cities')
    if cursor.fetchone()[0] == 0:
        cities = [
            ('London', 51.5074, -0.1278),
            ('Paris', 48.8566, 2.3522),
            ('Berlin', 52.5200, 13.4050),
            ('Madrid', 40.4168, -3.7038),
            ('Rome', 41.9028, 12.4964),
            ('Vienna', 48.2082, 16.3738),
            ('Amsterdam', 52.3676, 4.9041),
            ('Brussels', 50.8503, 4.3517),
            ('Prague', 50.0755, 14.4378),
            ('Budapest', 47.4979, 19.0402),
            ('Warsaw', 52.2297, 21.0122),
            ('Stockholm', 59.3293, 18.0686),
            ('Oslo', 59.9139, 10.7522),
            ('Copenhagen', 55.6761, 12.5683),
            ('Helsinki', 60.1695, 24.9354),
            ('Athens', 37.9838, 23.7275),
            ('Dublin', 53.3498, -6.2603),
            ('Lisbon', 38.7223, -9.1393),
            ('Bratislava', 48.1486, 17.1077),
            ('Ljubljana', 46.0569, 14.5058),
            ('Zagreb', 45.8150, 15.9819),
            ('Bern', 46.9480, 7.4474),
            ('Riga', 56.9496, 24.1052),
            ('Tallinn', 59.4370, 24.7536),
            ('Vilnius', 54.6872, 25.2797)
        ]
        # cities = [
        #     ('Baghdad', 33.3152, 44.3661),
        #     ('Duhok', 36.8667, 42.9667),
        #     ('Erbil', 41.8781, 40.7796),
        #     ('Mosul', 29.7604, 42.3314),
        #     ('Kirkuk', 33.4484, 44.8650),
        #     ('Basra', 30.5085, 47.7835),
        #     ('Najaf', 31.9959, 44.3148),
        #     ('Karbala', 32.6167, 44.0333),
        #     ('Sulaymaniyah', 35.5600, 45.4300),
        #     ('Zakho', 37.1436, 42.6869),
        #     ('Halabja', 35.1778, 45.9861),
        #     ('Kifri', 33.9333, 44.5833),
        #     ('Al-Qadisiyyah', 32.0000, 44.0000),
        #     ('Al-Muthanna', 30.0000, 45.0000),
        #     ('Al-Anbar', 33.0000, 43.0000),
        #     ('Wasit', 32.0000, 46.0000),
        #     ('Dhi Qar', 31.0000, 46.0000),
        #     ('Maysan', 32.0000, 47.0000),
        #     ('Nasiriya', 31.0000, 46.0000),
        #     ('Samawa', 31.0000, 45.0000),
        #     ('Amara', 31.0000, 47.0000),
        #     ('Hilla', 32.0000, 44.0000),
        #     ('Diwaniyah', 31.0000, 44.0000),
        #     ('Kut', 32.0000, 45.0000),
        #     ('Zubair', 30.0000, 47.0000),
        #     ('Baquba', 33.0000, 44.0000),
        #     ('Falluja', 33.0000, 43.0000),
        #     ('Ramadi', 33.0000, 42.0000),
        #     ('Abu al-Khasib', 30.0000, 47.0000),
        #     ('Al-Shatrah', 31.0000, 45.0000),
        #     ('Tal Afar', 36.0000, 42.0000),
        #     ('Kufa', 32.0000, 44.0000),
        #     ('Kalar', 35.0000, 45.0000),
        #     ('Shatt al-Arab', 30.0000, 47.0000),
        #     ('Soran', 36.0000, 44.0000),
        #     ('Suq al-Shuyukh', 31.0000, 45.0000),
        #     ('Al-shamal', 36.0000, 43.0000),
        #     ('Al-Qurnah', 30.0000, 47.0000),
        #     ('Al-Wahda', 31.0000, 44.0000),
        #     ('Tikrit', 34.0000, 43.0000),
        #     ('Tuz Khurmatu', 34.0000, 44.0000),
        #     ('Al-Mahmudiya', 33.0000, 44.0000),
        #     ('Iskandariya', 32.0000, 44.0000),
        #     ('Al-Mejar Al-Kabir', 31.0000, 45.0000),
        #     ('Ranya', 36.0000, 45.0000),
        #     ('Hamza', 31.0000, 44.0000),
        #     ('Al-Rumaitha', 30.0000, 46.0000),
        #     ('Al-Hayy', 31.0000, 45.0000),
        #     ('Al-Hindiyah', 31.0000, 44.0000),
        #     ('Baiji', 34.0000, 43.0000),
        #     ('Al-Qasim', 32.0000, 44.0000),
        #     ('Muqdadiyah', 34.0000, 45.0000),
        #     ('Al-Suwaira', 31.0000, 45.0000),
        #     ('Al-Rifai', 31.0000, 44.0000),
        #     ('Al-Qaim', 34.0000, 42.0000),
        #     ('Qaladiza', 36.0000, 45.0000),
        #     ('Simmele', 36.0000, 44.0000),
        #     ('An Numaniyah', 32.0000, 44.0000),
        #     ('Faydah', 31.0000, 45.0000),
        #     ('Akre', 36.0000, 44.0000),
        #     ('Halabja', 35.0000, 46.0000),
        #     ('Hit', 33.0000, 42.0000),
        #     ('Kasnazan', 36.0000, 44.0000),
        #     ('Chamchamal', 36.0000, 45.0000),
        #     ('Balad Ruz', 36.0000, 45.0000),
        #     ('Al Nasr Wa Al-Salam', 31.0000, 44.0000),
        #     ('Al Khalis', 31.0000, 45.0000),
        #     ('Jalawla', 31.0000, 45.0000),
        #     ('Koy Sanjaq', 36.0000, 44.0000),
        #     ('Said Sadiq', 36.0000, 45.0000),
        #     ('Balad', 33.0000, 44.0000),
        #     ('Al Midhatiya', 32.0000, 44.0000),
        #     ('Bnaslawa', 36.0000, 45.0000),
        #     ('Al-Shamiya', 31.0000, 44.0000),
        #     ('Musayyib', 31.0000, 44.0000),
        #     ('Qahtaniya', 36.0000, 45.0000),
        #     ('Qasrok', 36.0000, 44.0000),
        #     ('Al-Aziziyah', 31.0000, 45.0000),
        #     ('Al-Shirqat', 34.0000, 43.0000),
        #     ('Haji Awa', 31.0000, 44.0000),
        #     ('Qalat Sukkar', 31.0000, 45.0000),
        #     ('Khanaqin', 33.0000, 45.0000),
        #     ('Al-Nasr', 31.0000, 44.0000),
        #     ('Umm Qasr', 30.0000, 47.0000),
        # ]
        cursor.executemany('INSERT INTO cities (name, lat, lon) VALUES (?, ?, ?)', cities)
        conn.commit()

    else:
        print("Cities already exist in the database.")


def get_cities():
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, lat, lon FROM cities')
    cities = cursor.fetchall()
    return [{'id': row[0], 'name': row[1], 'lat': row[2], 'lon': row[3]} for row in cities]