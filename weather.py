import requests

def get_weather(city):
    api_key = "9a30d5974888518138425a9a08908cf1"  
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    try:
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data['cod'] == 200:  # Successful response
            print(f"Weather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Conditions: {data['weather'][0]['description']}")
            print(f"Humidity: {data['main']['humidity']}%")
        else:
            print(f"Error: {data['message']}")
    except Exception as e:
        print(f"Failed to fetch weather: {e}")

# Example usage
get_weather("Olongapo")