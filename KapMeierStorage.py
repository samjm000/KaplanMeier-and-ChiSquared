##PS KM Curve
from dataclasses import dataclass


@dataclass
class Storage:
    file: str
    data_set_name_1: str
    data_set_name_2: str


# Usage
# storage = Storage(file="KM-OS.xlsx", data_set_1="PS0-1", data_set_2="PS2-3")
# print(storage)  # Output: Storage(file='KM-OS.xlsx', data_set_1='PS0-1', data_set_2='PS2-3')
# print(storage.file)  # Output: KM-OS.xlsx
