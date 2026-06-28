from f1_client import F1Client
import pandas as pd
from datetime import datetime
import requests
import os

base_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(os.path.dirname(base_path))

year= datetime.now().year

target_dir = os.path.join(root_path, "data", "raw", f"season={year}")

os.makedirs(target_dir, exist_ok=True)

parquet_save_path = os.path.join(target_dir, "races.parquet")
json_save_path = os.path.join(target_dir, "races.json")

session = requests.Session()
client = F1Client(session, year)

races_data = client.get_races()

print(races_data)

df_races = pd.DataFrame(races_data['MRData']['RaceTable']['Races'])
df_races.to_parquet(parquet_save_path, index=False)
df_races.to_json(json_save_path, orient="records", indent=4)

session.close()