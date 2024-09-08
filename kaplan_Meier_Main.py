import numpy as np
import pandas as pd
import KapMeierStorage as km_storage
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
import matplotlib.pyplot as plt
import KM_Data_Builder

####### KAPLAN MAEIER DATA ############
# Load the data set wanted - options
# 1. Stage 3 vs. Stage 4
# 2. Age <75 vs. Age ≥75
# 3. PS 0-1 vs. PS ≥2 = PS_KM_Data : "Data/KM-PS.xlsx", "PS0-1", "PS2-3"
# 4. SMID 1-2 vs. SMID 3-5
# 5. Non-emergency vs. Emergency Presentation

# import from desired dataset
# data = KM_Data_Builder.get_data("Data/Ovarian PD.xlsx", "PS0-1", "PS2-3")
# data = KM_Data_Builder.get_data("Data/Ovarian PD.xlsx", "Age<75", "Age>75")
# data = KM_Data_Builder.get_data("Data/Ovarian PD.xlsx", "Stage 3", "Stage 4")
# data = KM_Data_Builder.get_data("Data/Ovarian PD.xlsx", "SMID 1-2", "SMID 3-5")
data = KM_Data_Builder.get_data(
    "Data/Ovarian PD.xlsx", "Emergency Presentation", "Non Emergency Presentation"
)


# Combine the DataFrames
df = pd.concat([data[0], data[1]])

# Convert columns to datetime
df["diagnosis"] = pd.to_datetime(df["diagnosis"])
df["death"] = pd.to_datetime(df["death"], errors="coerce")

# Set the date of last follow-up for missing date of death to 1st Jan 2024
df["death"].fillna(pd.Timestamp("2024-01-01"), inplace=True)

# Calculate survival time
df["survival_time"] = (df["death"] - df["diagnosis"]).dt.days

# Create event indicator (1 if death occurred, 0 if censored)
df["event"] = df["death"].notnull().astype(int)

# Fit Kaplan-Meier curves
kmf = KaplanMeierFitter()

# Apply a Matplotlib style
plt.style.use("fivethirtyeight")

# Plot for data sets
ax = None
groups = df["group"].unique()
for group in df["group"].unique():
    kmf.fit(
        df["survival_time"][df["group"] == group],
        event_observed=df["event"][df["group"] == group],
        label=group,
    )
    ax = kmf.plot_survival_function(ax=ax)


# Customize the plot title dynamically
title = f"Kaplan-Meier Survival Curves: {' vs '.join(groups)}"
plt.title(title, fontsize=14)
plt.xlabel("Time (days)", fontsize=12)
plt.ylabel("Survival Probability", fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()
