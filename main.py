import sys
from weather_client import WeatherClient

while True:
    menu = 0
    client = WeatherClient()
    list = client.list_cities()
    print("Which city would you like to view the weather?")
    print("-" * 40)
    for index, list in enumerate(list, start=1):
        print(f"{index}. {list}")
    print("-" * 40)
    menu = input("Type in the number next to the city: ")
    if menu == "1":
        temp = client.fetch_current("Johannesburg")["current"][
            "temperature_2m"
            ]
        temp_unit = client.fetch_current("Johannesburg")["current_units"][
            "temperature_2m"
        ]
        weather_condition = client.weather_code(
            client.fetch_current("Johannesburg")["current"]["weather_code"]
        )
        print("-" * 40)
        print("Johannesburg (Today):")
        print(f"Temperature: {temp}{temp_unit} Weather: {weather_condition}")
        print("-" * 40)
        while True:
            again = input("See another city? (Y/N): ").upper().strip()
            if again == "N":
                print("-" * 40)
                sys.exit()
            elif again == "Y":
                print("-" * 40)
                break
            else:
                print("-" * 40)
                print("Invalid. Only type Y or N")
                print("-" * 40)
    elif menu == "2":
        temp = client.fetch_current("Cape Town")["current"]["temperature_2m"]
        temp_unit = client.fetch_current("Cape Town")["current_units"][
            "temperature_2m"]
        weather_condition = client.weather_code(
            client.fetch_current("Cape Town")["current"]["weather_code"]
        )
        print("-" * 40)
        print("Cape Town (Today):")
        print(f"Temperature: {temp}{temp_unit} Weather: {weather_condition}")
        print("-" * 40)
        while True:
            again = input("See another city? (Y/N): ").upper().strip()
            if again == "N":
                print("-" * 40)
                sys.exit()
            elif again == "Y":
                print("-" * 40)
                break
            else:
                print("-" * 40)
                print("Invalid. Only type Y or N")
                print("-" * 40)
    elif menu == "3":
        temp = client.fetch_current("Durban")["current"]["temperature_2m"]
        temp_unit = client.fetch_current("Durban")["current_units"][
            "temperature_2m"]
        weather_condition = client.weather_code(
            client.fetch_current("Durban")["current"]["weather_code"]
        )
        print("-" * 40)
        print("Durban (Today):")
        print(f"Temperature: {temp}{temp_unit} Weather: {weather_condition}")
        print("-" * 40)
        while True:
            again = input("See another city? (Y/N): ").upper().strip()
            if again == "N":
                print("-" * 40)
                sys.exit()
            elif again == "Y":
                print("-" * 40)
                break
            else:
                print("-" * 40)
                print("Invalid. Only type Y or N")
                print("-" * 40)
    elif menu == "4":
        temp = client.fetch_current("Pretoria")["current"][
            "temperature_2m"]
        temp_unit = client.fetch_current("Pretoria")["current_units"][
            "temperature_2m"]
        weather_condition = client.weather_code(
            client.fetch_current("Pretoria")["current"]["weather_code"]
        )
        print("-" * 40)
        print("Pretoria (Today):")
        print(f"Temperature: {temp}{temp_unit} Weather: {weather_condition}")
        print("-" * 40)
        while True:
            again = input("See another city? (Y/N): ").upper().strip()
            if again == "N":
                print("-" * 40)
                sys.exit()
            elif again == "Y":
                print("-" * 40)
                break
            else:
                print("-" * 40)
                print("Invalid. Only type Y or N")
                print("-" * 40)
    elif menu == "5":
        temp = client.fetch_current("Port Elizabeth")["current"][
            "temperature_2m"]
        temp_unit = client.fetch_current("Port Elizabeth")["current_units"][
            "temperature_2m"
        ]
        weather_condition = client.weather_code(
            client.fetch_current("Port Elizabeth")["current"]["weather_code"]
        )
        print("-" * 40)
        print("Port Elizabeth (Today):")
        print(f"Temperature: {temp}{temp_unit} Weather: {weather_condition}")
        print("-" * 40)
        while True:
            again = input("See another city? (Y/N): ").upper().strip()
            if again == "N":
                print("-" * 40)
                sys.exit()
            elif again == "Y":
                print("-" * 40)
                break
            else:
                print("-" * 40)
                print("Invalid. Only type Y or N")
                print("-" * 40)
    else:
        print("-" * 40)
        print("Invaild Number. Please enter the correct number")
        print("-" * 40)
