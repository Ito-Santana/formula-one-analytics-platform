from f1_client import F1Client
import requests
from datetime import datetime
import pandas as pd
import os

base_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(os.path.dirname(base_path))

year= datetime.now().year

target_dir = os.path.join(root_path, "data", "raw", f"season={year}")

os.makedirs(target_dir, exist_ok=True)

parquet_save_path = os.path.join(target_dir, "drivers.parquet")
json_save_path = os.path.join(target_dir, "drivers.json")

session = requests.Session()
client = F1Client(session, year)

drivers_data = client.get_drivers()

df_drivers = pd.DataFrame(drivers_data['MRData']['DriverTable']['Drivers'])
df_drivers.to_parquet(parquet_save_path, index=False)
df_drivers.to_json(json_save_path, orient="records", indent=4)

session.close()