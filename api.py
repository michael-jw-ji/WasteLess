from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from io import StringIO
from pathlib import Path

import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parent
MODEL_DIR = ROOT / "models_dir"

MODEL = joblib.load(MODEL_DIR / "forecast_qty_used_rf.joblib")
FEATURE_COLS = joblib.load(MODEL_DIR / "forecast_feature_cols.joblib")

REQUIRED_COLS = [
    "date",
    "dish_id",
    "dish_name",
    "category",
    "qty_sold",
    "restaurant_id",
    "price",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/upload-sales")
async def upload_sales(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="File must be a .csv")

    raw_bytes = await file.read()
    try:
        text = raw_bytes.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="CSV must be utf-8 encoded")

    df = pd.read_csv(StringIO(text))

    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise HTTPException(
            status_code=400,
            detail=f"Missing required columns: {', '.join(missing)}",
        )

    # Basic cleanup to align with training code
    df["date"] = pd.to_datetime(df["date"])
    df["day_of_week"] = df["date"].dt.weekday

    # Build a minimal feature frame similar to train_model.py
    feature_df = pd.get_dummies(
        df[["category", "day_of_week"]],
        columns=["category"],
    )

    # Align columns with the model's expected feature columns
    for col in FEATURE_COLS:
        if col not in feature_df.columns:
            feature_df[col] = 0
    feature_df = feature_df[FEATURE_COLS]

    preds = MODEL.predict(feature_df)
    df["predicted_qty_used_kg"] = preds

    preview_cols = [
        "date",
        "dish_name",
        "category",
        "qty_sold",
        "predicted_qty_used_kg",
    ]

    rows = (
        df[preview_cols]
        .head(200)  # avoid huge payloads
        .to_dict(orient="records")
    )

    return {"rows": rows}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)


