import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
import matplotlib.pyplot as plt

# Function to perform chi-square test and print results
def chi_square_test(data, comparison_name):
    chi2, p, dof, expected = chi2_contingency(data)
    print(f"{comparison_name}:\nChi2: {chi2}, p-value: {p}\n")

# 1. Stage 3 vs. Stage 4
data_stage = np.array([[14, 59], [8, 38]])
chi_square_test(data_stage, "Stage 3 vs Stage 4")

# 2. Age <75 vs. Age ≥75
data_age = np.array([[15, 66], [7, 31]])
chi_square_test(data_age, "Age <75 vs Age ≥75")

# 3. PS 0-1 vs. PS ≥2
data_ps = np.array([[16, 86], [6, 11]])
chi_square_test(data_ps, "PS 0-1 vs PS ≥2")

# 4. SMID 1-2 vs. SMID 3-5
data_smid = np.array([[14, 40], [8, 57]])  # SMID 1-2 vs. SMID 3-5
chi_square_test(data_smid, "SMID 1-2 vs SMID 3-5")

# 5. Non-emergency vs. Emergency Presentation
data_presentation = np.array([[13, 66], [9, 31]])
chi_square_test(data_presentation, "Non-emergency vs Emergency Presentation")

# Convert to DataFrame

# Load the data from both tabs
df_ps_0_1 = pd.read_excel('KM-PS.xlsx', sheet_name='PS0-1')
df_ps_2_3 = pd.read_excel('KM-PS.xlsx', sheet_name='PS2-3')

# Add a group column to each DataFrame
df_ps_0_1['group'] = 'PS 0-1'
df_ps_2_3['group'] = 'PS 2-3'

# Combine the DataFrames
df = pd.concat([df_ps_0_1, df_ps_2_3])

# Convert columns to datetime
df['diagnosis'] = pd.to_datetime(df['diagnosis'])
df['death'] = pd.to_datetime(df['death'], errors='coerce')

# Set the date of last follow-up for missing date of death to 1st Jan 2024
df['death'].fillna(pd.Timestamp('2024-01-01'), inplace=True)

# Calculate survival time
df['survival_time'] = (df['death'] - df['diagnosis']).dt.days

# Create event indicator (1 if death occurred, 0 if censored)
df['event'] = df['death'].notnull().astype(int)

# Fit Kaplan-Meier curves
kmf = KaplanMeierFitter()

# Apply a Matplotlib style
plt.style.use('fivethirtyeight')

# Plot for PS 0-1
kmf.fit(df['survival_time'][df['group'] == 'PS 0-1'], event_observed=df['event'][df['group'] == 'PS 0-1'], label='PS 0-1')
ax = kmf.plot_survival_function()

# Plot for PS 2-3
kmf.fit(df['survival_time'][df['group'] == 'PS 2-3'], event_observed=df['event'][df['group'] == 'PS 2-3'], label='PS 2-3')
kmf.plot_survival_function(ax=ax)

# Customize the plot
plt.title('Kaplan-Meier Survival Curves: PS 0-1 vs PS 2-3', fontsize=14)
plt.xlabel('Time (days)', fontsize=12)
plt.ylabel('Survival Probability', fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()