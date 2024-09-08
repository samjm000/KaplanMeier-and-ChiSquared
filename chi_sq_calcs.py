from scipy.stats import chi2_contingency
import numpy as np


# Function to perform chi-square test and print results
def chi_square_test(data, comparison_name):
    chi2, p, dof, expected = chi2_contingency(data)
    print(f"{comparison_name}:\nChi2: {chi2}, p-value: {p}\n")


if __name__ == "__main__":
    print("Running CHi 2")


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
