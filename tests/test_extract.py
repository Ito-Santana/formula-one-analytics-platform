import pytest
import requests

from unittest.mock import Mock

from src.extract.f1_client import F1Client


@pytest.fixture
def f1_client():
    session = requests.Session()
    client = F1Client(session=session, year=2026)

    yield client

    session.close()


class TestF1Client:
    def test_f1_client_initialization(self, f1_client):
        assert f1_client.year == 2026
        assert isinstance(f1_client.session, requests.Session)
    
    def test_get_drivers(self, f1_client):
        drivers = f1_client.get_drivers()

        assert "MRData" in drivers
        assert "DriverTable" in drivers["MRData"]
        assert "Drivers" in drivers["MRData"]["DriverTable"]

    def test_get_drivers_exception(self, f1_client, monkeypatch):
        # Mock the session.get method to raise an exception
        monkeypatch.setattr(f1_client.session, "get", Mock(side_effect=requests.RequestException("Network error")))

        with pytest.raises(requests.RequestException):
            f1_client.get_drivers()

    def test_get_races(self, f1_client):
        races = f1_client.get_races()

        assert "MRData" in races
        assert "RaceTable" in races["MRData"]
        assert "Races" in races["MRData"]["RaceTable"]
    
    def test_get_races_exception(self, f1_client, monkeypatch):
        # Mock the session.get method to raise an exception
        monkeypatch.setattr(f1_client.session, "get", Mock(side_effect=requests.RequestException("Network error")))

        with pytest.raises(requests.RequestException):
            f1_client.get_races()

    def test_get_constructors(self, f1_client):
        constructors = f1_client.get_constructors()

        assert "MRData" in constructors
        assert "ConstructorTable" in constructors["MRData"]
        assert "Constructors" in constructors["MRData"]["ConstructorTable"]
    
    def test_get_constructors_exception(self, f1_client, monkeypatch):
        # Mock the session.get method to raise an exception
        monkeypatch.setattr(f1_client.session, "get", Mock(side_effect=requests.RequestException("Network error")))

        with pytest.raises(requests.RequestException):
            f1_client.get_constructors()