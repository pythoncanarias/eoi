from datetime import datetime
import pytz

if __name__ == '__main__':
    places_tz = [
        'Asia/Tokyo', 'Europe/Madrid', 'America/Argentina Buenos_Aires', 'US/eastern', 'US/Pacific', 'UTC'
    ]
    
    cities_name = ['Tokyo', 'Madrid', 'Buenos Aires', 'New York', 'California', 'UTC']    
    
    for place_tz, city_name in zip(places_tz, cities_name) :
        city_time = datetime.now(pytz.timezone(place_tz))
        print(f'Fecha en {city_name} - {city_time}')