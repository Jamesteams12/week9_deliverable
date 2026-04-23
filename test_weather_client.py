from weather_client import WeatherClient

c = WeatherClient()

def test_client_has_cities():
    assert "Johannesburg" in c.list_cities()

def test_unknown_city_returns_none():
    assert c.fetch_current("Atlantis") is None

def test_fetch_current_returns_dict():
    assert type(c.fetch_current("Johannesburg")) is dict