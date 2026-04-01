# 🌦️ Weather Data Extraction Pipeline

> **v1.0.0** — A clean, secure ETL pipeline for extracting and storing historical weather data using the WeatherAPI.

---

## 👤 Author

**Harsh Raj Gupta**
- GitHub: [@The-Noob-Developer](https://github.com/The-Noob-Developer)
- Email: [itsokaytobeharsh@gmail.com](mailto:itsokaytobeharsh@gmail.com)

---

## 📌 Overview

This project extracts historical weather data using the **WeatherAPI (Free Plan)**, processes it into a structured format using Python, and stores the results in a CSV file. The pipeline is designed to be secure, reproducible, and extendable for production use.

---

## ✨ Features

- 🔐 Secure API key management using `.env`
- 📅 Dynamic date range extraction
- ⚠️ Robust error handling for API failures
- 💾 Data persistence with append (no overwrite)
- 🧹 Duplicate handling based on date and location
- 🧱 Clean and modular code structure

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas | Data processing & CSV management |
| Requests | HTTP API calls |
| python-dotenv | Secure environment variable management |

---

## 📁 Project Structure

```
weather-api-capstone/
│── main.py              # Main ETL script
│── .env                 # API key (not committed)
│── .gitignore           # Excludes .env and other sensitive files
│── requirements.txt     # Project dependencies
│── weather.csv          # Output data file
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/The-Noob-Developer/weather-api-capstone.git
cd weather-api-capstone
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:

```env
WEATHER_API_KEY=your_api_key_here
```

Add `.env` to `.gitignore`:

```
.env
```

> 🔑 Get your free API key at [weatherapi.com](https://www.weatherapi.com)

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Provide inputs when prompted:

```
Enter location: Kolkata
Enter start date (YYYY-MM-DD): 2026-02-02
Enter end date (YYYY-MM-DD): 2026-02-05
```

---

## 📤 Output

- Data is saved in `weather.csv`
- Existing data is preserved on each run
- New data is appended
- Duplicate entries are removed based on **date + location**

### 📋 Output Columns

| Column | Description |
|---|---|
| `date` | Date of the record |
| `location` | City / location name |
| `avg_temp_c` | Average temperature (°C) |
| `max_temp_c` | Maximum temperature (°C) |
| `min_temp_c` | Minimum temperature (°C) |
| `max_wind_kph` | Maximum wind speed (kph) |
| `total_precip_mm` | Total precipitation (mm) |
| `total_snow_cm` | Total snowfall (cm) |
| `avg_humidity` | Average humidity (%) |
| `avg_visibility_km` | Average visibility (km) |
| `condition` | Weather condition description |
| `uv_index` | UV index value |
| `will_rain` | Rain indicator (0/1) |
| `chance_of_rain` | Probability of rain (%) |
| `will_snow` | Snow indicator (0/1) |
| `chance_of_snow` | Probability of snow (%) |
| `sunrise` / `sunset` | Sunrise and sunset times |
| `moonrise` / `moonset` | Moonrise and moonset times |
| `moon_phase` | Lunar phase name |
| `moon_illumination` | Moon illumination (%) |
| `start_date` / `end_date` | Query date range |

### 🗂️ Sample Data

```csv
date,location,avg_temp_c,max_temp_c,min_temp_c,max_wind_kph,total_precip_mm,total_snow_cm,avg_humidity,avg_visibility_km,condition,uv_index,will_rain,chance_of_rain,will_snow,chance_of_snow,sunrise,sunset,moonrise,moonset,moon_phase,moon_illumination,start_date,end_date
2026-03-30,Hyderabad,31.5,36.6,27.4,23.8,0.9,0.0,33,10.0,Moderate rain at times,11.8,1,100,0,0,06:12 AM,06:29 PM,04:14 PM,04:16 AM,Waxing Gibbous,88,2026-03-30,2026-03-31
2026-02-02,Kolkata,22.2,28.9,16.3,13.0,0.0,0.0,26,10.0,Sunny,3.7,0,0,0,0,06:15 AM,05:26 PM,05:57 PM,06:30 AM,Full Moon,100,2026-02-02,2026-02-05
```

---

## 🚨 Error Handling

- API errors are captured and logged to the console
- Invalid date ranges are handled gracefully
- Empty datasets are not written to file

---

## 📦 Requirements Generation

To auto-generate dependencies:

```bash
pipreqs . --force
```

Or capture the full environment:

```bash
pip freeze > requirements.txt
```

---

## ⚠️ Limitations

- WeatherAPI **free tier** restricts historical data access (limited date range)
- Older dates may return no data
- Rate limits may apply on the free plan

---

## 🚀 Future Improvements

- [ ] Azure Data Factory (ADF) integration
- [ ] Logging system using the `logging` module
- [ ] Database integration (SQL / Azure Blob Storage)
- [ ] Scheduled automation (cron / Apache Airflow)
- [ ] API retry mechanism with exponential backoff

---

## 📄 Conclusion

This project demonstrates a clean, production-minded ETL pipeline for weather data with secure credential management, structured output, and scalable design — ready for extension into real-world data engineering workflows.

---

*Built with ❤️ by [Harsh Raj Gupta](https://github.com/The-Noob-Developer)*