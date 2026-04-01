import requests
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# ---------------- LOAD ENV ----------------
load_dotenv(dotenv_path=".env")

API_KEY = os.getenv("WEATHER_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Please set WEATHER_API_KEY in .env file")

# ---------------- INPUT ----------------
LOCATION = input("Enter location: ")
START_DATE = input("Enter start date (YYYY-MM-DD): ")
END_DATE = input("Enter end date (YYYY-MM-DD): ")

# ----------------------------------------


def fetch_weather(date, location):
    url = f"http://api.weatherapi.com/v1/history.json?key={API_KEY}&q={location}&dt={date}"
    response = requests.get(url)
    data = response.json()

    # Handle API errors
    if "error" in data:
        raise Exception(data["error"]["message"])

    forecastday = data['forecast']['forecastday'][0]
    day = forecastday['day']
    astro = forecastday['astro']

    return {
        "date": date,
        "location": location,

        "avg_temp_c": day.get('avgtemp_c'),
        "max_temp_c": day.get('maxtemp_c'),
        "min_temp_c": day.get('mintemp_c'),

        "max_wind_kph": day.get('maxwind_kph'),

        "total_precip_mm": day.get('totalprecip_mm'),
        "total_snow_cm": day.get('totalsnow_cm'),

        "avg_humidity": day.get('avghumidity'),
        "avg_visibility_km": day.get('avgvis_km'),

        "condition": day.get('condition', {}).get('text'),

        "uv_index": day.get('uv'),

        "will_rain": day.get('daily_will_it_rain'),
        "chance_of_rain": day.get('daily_chance_of_rain'),
        "will_snow": day.get('daily_will_it_snow'),
        "chance_of_snow": day.get('daily_chance_of_snow'),

        "sunrise": astro.get('sunrise'),
        "sunset": astro.get('sunset'),
        "moonrise": astro.get('moonrise'),
        "moonset": astro.get('moonset'),
        "moon_phase": astro.get('moon_phase'),
        "moon_illumination": astro.get('moon_illumination')
    }


def get_date_range(start, end):
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")

    dates = []
    while start <= end:
        dates.append(start.strftime("%Y-%m-%d"))
        start += timedelta(days=1)

    return dates


def extract_data():
    dates = get_date_range(START_DATE, END_DATE)
    results = []

    for d in dates:
        print(f"Fetching data for {d}")
        try:
            row = fetch_weather(d, LOCATION)
            row["start_date"] = START_DATE
            row["end_date"] = END_DATE
            results.append(row)
        except Exception as e:
            print(f"Error on {d}: {e}")

    df = pd.DataFrame(results)

    if df.empty:
        print("No data fetched. Check API/date range.")
        return None

    return df


def save_to_csv(df):
    file_name = "weather.csv"

    if df is None:
        print("Nothing to save.")
        return

    if os.path.exists(file_name):
        existing_df = pd.read_csv(file_name)
        combined_df = pd.concat([existing_df, df]).drop_duplicates()
        combined_df.to_csv(file_name, index=False)
        print("Data appended + duplicates removed")
    else:
        df.to_csv(file_name, index=False)
        print("New CSV created")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    df = extract_data()

    if df is not None:
        print(df.head())
        save_to_csv(df)