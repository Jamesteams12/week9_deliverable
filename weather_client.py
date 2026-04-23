import requests


class WeatherClient:
    """
    Link for the API
    City coordinates
    """
    base_url = "https://api.open-meteo.com/v1/forecast"
    city = {
        "Johannesburg": (-26.2041, 28.0473),
        "Cape Town": (-33.9249, 18.4241),
        "Durban": (-29.8587, 31.0218),
        "Pretoria": (-25.7479, 28.2293),
        "Port Elizabeth": (-33.9608, 25.6022),
    }

    def __init__(self, timeout :int=10):
        """
        Timeout timer for when it takes too long
        """
        self.timeout = timeout

    def fetch_current(self, city_name :any ):
        """
        Gets the city from the list, if can't find then it return none
        otherwise it creates lat and lon cords and a url
        """
        if city_name not in self.city:
            return None
        lat, lon = self.city[city_name]
        url = f"{self.base_url}?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code"

        try:
            """
            Test to see if the API url is working ot not
            """
            r = requests.get(url, self.timeout)
            r.raise_for_status()  # raises HTTPError if 4xx/5xx
            return r.json()
        except requests.exceptions.Timeout:
            print(f"Error: {url} took too long to respond")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"Error: HTTP {e.response.status_code} from {url}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error: could not reach {url}: {e}")
            return None
        except ValueError:
            print(f"Error: response from {url} was not valid JSON")
            return None

    def list_cities(self):
        """
        Shows a list of all city avaliable
        """
        return list(self.city.keys())

    def weather_code(self, number :any):
        """
        A weather code to say what is the weather in the city
        """
        self.number = 0
        if number == 0:
            return "Clear/Sunny"
        elif number == 1:
            return "Partly Cloudy"
        elif number == 2:
            return "Cloudy"
        elif number == 3:
            return "Overcast"
        elif number == 4:
            return "Fog"
        elif number == 5:
            return "Drizzle"
        elif number == 6:
            return "Rain"
        elif number == 7:
            return "Snow"
        elif number == 8:
            return "Shower(s)"
        elif number == 9:
            return "Thunderstorm"
        else:
            return None
