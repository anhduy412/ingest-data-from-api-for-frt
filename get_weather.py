import requests
import csv

province_list = [
    # 'An Giang', 'Bắc Ninh', 'Cao Bằng', 'Cà Mau', 'Gia Lai', # 'Hà Nội', 'Hà Tĩnh', 'Hòa Bình', 'Hưng Yên', 'Lai Châu',
    # 'Lào Cai', 'Lâm Đồng', 'Lạng Sơn', 'Nghệ An', 'Ninh Bình', 'Ninh Thuận', 'Quảng Ngãi', 
    'Quảng Ninh', 'Quảng Trị', 'Sơn La', 'Thanh Hóa', 'Thành phố Cần Thơ', 'Hải Phòng',
    'Thành phố Hồ Chí Minh', 'Thái Nguyên', 'Tuyên Quang', 'Tây Ninh', 'Vĩnh Long', 'Điện Biên', 
    'Đà Nẵng', 'Đắk Lắk', 'Đồng Nai', 'Đồng Tháp', 'Thừa Thiên Huế'
]
lat_list = [
    # 10.267, 21.2335, 22.6657, 9.2354, 13.8828, # 21.0285, 18.3428, 21.1911, 20.5485, 22.3862,
    # 22.0955, 11.7712, 21.8537, 18.6731, 20.4113, # 11.9032, 14.7352, 
    21.005, 17.1433, 21.3274, 19.8066, 9.6806, 20.9373,
    10.7317, 21.8706, 22.3233, 10.9271, 10.1417, 21.386, 
    15.7932, 12.8848, 11.3508, 10.4157, 16.4637
]
lon_list = [
    # 105.1031, 106.137, 106.257, 105.4384, 108.61, # 105.8542, 105.9057, 105.3987, 106.1966, 103.4586,
    # 104.4208, 108.0548, 106.7615, 105.6923, 106.0195, # 109.0926, 108.3884, 
    107.2925, 106.857, 103.9144, 105.7852, 105.811, 106.3147,
    106.8303, 105.8414, 105.099, 106.2562, 106.2311, 103.023, 
    108.1064, 108.6828, 106.8741, 105.9826, 107.5909
]

# Define date range
start_date = '2023-01-01'
end_date = '2025-08-07'

# open CSV file for writing
with open('weather.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['province', 'date', 'max_temp', 'min_temp', 'humidity', 'precipitation'])

    for province, lat, lon in zip(province_list, lat_list, lon_list):
        url = f'https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,relative_humidity_2m_max,relative_humidity_2m_min&timezone=Asia%2FBangkok'
        response = requests.get(url)
        data = response.json()
        for i in range(len(data['daily']['time'])):
            date = data['daily']['time'][i]
            temp_max = data['daily']['temperature_2m_max'][i]
            temp_min = data['daily']['temperature_2m_min'][i]
            humidity = data['daily']['relative_humidity_2m_max'][i]
            precipitation = data['daily']['precipitation_sum'][i]
            writer.writerow([province, date, temp_max, temp_min, humidity, precipitation])
            print(f'Processed {province} for date {date}')
print('Weather data collection completed successfully. The data has been saved to weather.csv.')