from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "data" / "raw" / "sales"
PROCESSED_DIR = ROOT / "data" / "processed"
INPUT_PATH = RAW_DIR / "Sales Dataset.csv"
OUTPUT_PATH = PROCESSED_DIR / "sales.csv"

# Read CSV sales dataset once it has been dropped into data/raw/sales/.
sales_raw = pd.read_csv(INPUT_PATH)  # adjust filename if needed

# Rename columns to the schema used by downstream forecasting code.
sales = sales_raw.rename(
    columns={
        "System Date": "date",
        "Food ID": "dish_id",
        "Food Name": "dish_name",
        "Food Category": "category",
        "Quantity": "qty_sold",
        "Restaurant Name": "restaurant_id",
        "Total Price": "price",
    }
)

sales["date"] = pd.to_datetime(sales["date"])

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
sales.to_csv(OUTPUT_PATH, index=False)

print(f"Wrote normalized sales data to {OUTPUT_PATH}")
