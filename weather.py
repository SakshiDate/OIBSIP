import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: Unable to fetch weather data for {city}.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        weather_condition = weather_data["weather"][0]["description"]

        print(f"\nWeather Information for {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Condition: {weather_condition}")
    else:
        print("Error: Unable to display weather information.")

def main():
    api_key = "59ce1cad91b40e62fb56746e620b6a99"  #API key
    city = input("Enter the city name: ")

    weather_data = get_weather(api_key, city)

    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
