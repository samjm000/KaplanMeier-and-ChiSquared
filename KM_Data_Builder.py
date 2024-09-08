# PS_KM_Curve.py

import KapMeierStorage as KM_Store
import pandas as pd


# Build PS Data
def get_data(file, data_set_name_1, data_set_name_2):
    """
    Load data from an Excel file and specified sheets.

    Parameters:
    file (str): The path to the Excel file.
    data_set_name_1 (str): The name of the first sheet.
    data_set_name_2 (str): The name of the second sheet.

    Returns:
    list: A list containing two DataFrames, one for each sheet.

    Example:
    get_data("Data/KM-PS.xlsx", "PS0-1", "PS2-3")
    [DataFrame for PS0-1, DataFrame for PS2-3]
    """

    storage = KM_Store.Storage(file, data_set_name_1, data_set_name_2)

    data_set_1 = pd.read_excel(storage.file, storage.data_set_name_1)
    data_set_2 = pd.read_excel(storage.file, storage.data_set_name_2)

    # Add a group column to each DataFrame
    data_set_1["group"] = data_set_name_1
    data_set_2["group"] = data_set_name_2

    data_set = [data_set_1, data_set_2]

    return data_set


if __name__ == "__main__":
    print("Running test")
    # print(get_data("Data/KM-PS.xlsx", "PS0-1", "PS2-3"))
    print(get_data("Data/Ovarian PD.xlsx", "SMID 1-2", "SMID 3-5"))
