import requests
import pandas as pd
from datetime import datetime, timedelta
from sqlalchemy import create_engine

# ---------------- CONFIG ----------------
API_KEY = "25a0a9250754489991645641263103"
LOCATION = input("Enter location: ")
START_DATE = input("Enter start date (YYYY-MM-DD): ")
END_DATE = input("Enter end date (YYYY-MM-DD): ")

# SQL Server credentials
DB_USER = "your_username"
DB_PASS = "your_password"
DB_SERVER = "your_server"
DB_NAME = "your_database"

# ----------------------------------------


def fetch_weather(date, location):
    url = f"http://api.weatherapi.com/v1/history.json?key={API_KEY}&q={location}&dt={date}"
    response = requests.get(url)
    data = response.json()

    day = data['forecast']['forecastday'][0]['day']

    return {
        "date": date,
        "location": location,
        "temp_c": day['avgtemp_c'],
        "humidity": day['avghumidity'],
        "wind_kph": day['maxwind_kph'],
        "condition": day['condition']['text']
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

            # add required fields
            row["start_date"] = START_DATE
            row["end_date"] = END_DATE

            results.append(row)
        except Exception as e:
            print(f"Error on {d}: {e}")

    return pd.DataFrame(results)


def save_to_csv(df):
    df.to_csv("weather.csv", index=False)
    print("CSV saved")


def load_to_sql(df):
    engine = create_engine(
        f"mssql+pyodbc://{DB_USER}:{DB_PASS}@{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server"
    )

    df.to_sql("weather_data", engine, if_exists="append", index=False)
    print("Data inserted into SQL Server")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    df = extract_data()

    print(df.head())

    save_to_csv(df)

    # Uncomment after DB setup is ready
    # load_to_sql(df)