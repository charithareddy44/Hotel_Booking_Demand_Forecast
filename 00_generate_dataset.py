import pandas as pd
import numpy as np

np.random.seed(42)

n = 10000

data = {
    "booking_id": np.arange(1, n+1),
    "hotel_type": np.random.choice(["Resort Hotel", "City Hotel"], n),
    "lead_time": np.random.randint(0, 365, n),
    "arrival_month": np.random.choice(
        ["January","February","March","April","May","June",
         "July","August","September","October","November","December"], n),
    "arrival_weekday": np.random.choice(
        ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], n),
    "stays_in_weekend_nights": np.random.randint(0, 5, n),
    "stays_in_week_nights": np.random.randint(1, 10, n),
    "adults": np.random.randint(1, 4, n),
    "children": np.random.choice([0,1,2,np.nan], n),
    "customer_type": np.random.choice(
        ["Transient","Contract","Group","Transient-Party"], n),
    "adr": np.round(np.random.uniform(50, 500, n), 2),
    "is_canceled": np.random.choice([0,1], n, p=[0.7,0.3])
}

df = pd.DataFrame(data)

# -----------------------------
# INTENTIONAL ERRORS
# -----------------------------

# Add duplicates
df = pd.concat([df, df.sample(200)], ignore_index=True)

# Add missing values
df.loc[df.sample(300).index, "adr"] = np.nan
df.loc[df.sample(200).index, "customer_type"] = np.nan

# Save dataset
df.to_csv("../data/raw/hotel_bookings_raw.csv", index=False)

print("Dataset created successfully!")
print("Shape:", df.shape)
print("Missing values:\n", df.isnull().sum())
