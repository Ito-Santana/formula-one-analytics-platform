from loguru import logger

import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"


class F1Client:
    def __init__(self, session, year):
        self.session = session
        self.year = year

    def get_drivers(self):
        url = f"{BASE_URL}/{self.year}/drivers/"

        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching drivers: {e}")
            raise e
        
    def get_races(self):
        url = f"{BASE_URL}/{self.year}/races/"

        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching races: {e}")
            raise e

    def get_constructors(self):
        url = f"{BASE_URL}/{self.year}/constructors/"

        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching constructors: {e}")
            raise e