from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_PATH = ROOT / "data" / "raw" / "weather" / "toronto_weather_2026.csv"

LATITUDE = 43.651070
LONGITUDE = -79.347015
BASE_URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "start_date": "2025-12-11",
    "end_date": "2026-03-13",
    "daily": "weathercode,temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "America/Toronto",
}

resp = requests.get(BASE_URL, params=params, timeout=30)
resp.raise_for_status()
data = resp.json()

if "daily" not in data:
    raise RuntimeError("No 'daily' in response, got: " + str(data))

daily = data["daily"]
df = pd.DataFrame(
    {
        "date": daily["time"],
        "weathercode": daily["weathercode"],
        "tmax_c": daily["temperature_2m_max"],
        "tmin_c": daily["temperature_2m_min"],
        "precip_mm": daily["precipitation_sum"],
    }
)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)
print(f"Saved weather data to {OUTPUT_PATH}")
