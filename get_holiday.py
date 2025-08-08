import requests
import pandas as pd

url = 'https://api.11holidays.com/v1/holidays?country=VN&year={year}'
year = ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033']
holiday = []
response = requests.get(url)

for years in year:
    response = requests.get(url.format(year=years))
    if response.status_code == 200:
        holidays = response.json()
        date = [holiday['date'] for holiday in holidays]
        name = [holiday['name'] for holiday in holidays]
        print(date, name)
    else:
        print(f"Failed to retrieve data: {response.status_code}")
    holiday.extend(zip(date, name))

holiday_df = pd.DataFrame(holiday, columns=['date', 'name'])
holiday_df['date'] = pd.to_datetime(holiday_df['date'])
holiday_df['year'] = holiday_df['date'].dt.year
holiday_df['month'] = holiday_df['date'].dt.month
holiday_df['day'] = holiday_df['date'].dt.day
holiday_df['date'] = holiday_df['date'].dt.strftime('%Y-%m-%d')
holiday_df.to_csv('holidays_vietnam.csv', index=False)
