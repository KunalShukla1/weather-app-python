import requests
import json
api_key = "your_API_Key"

basic_url = "https://api.openweathermap.org/data/2.5/weather"
City = input("Enter City Name: ")

params = {
    'q' : City,                                             #query parameter is used to specify the location for which the weather data is requested.
    'appid' : api_key,                                      #appid parameter is used to provide the API key for authentication.
    'units' : 'metric'                                      #units parameter is used to specify the unit of measurement for temperature (metric, imperial, or standard).
}
response = requests.get(basic_url, params=params)
# The requests.get() method is used to send a GET request to the specified URL with the provided query parameters.
# The response object contains the server's response to the request.

if response.status_code == 200:                                              # Check if the request was successful (status code 200 indicates success)
    data = response.json()                                                   #response.json() method is used to parse the JSON response from the server into a Python dictionary.
                                                                             # The data variable now contains the weather data for the specified city.
    print(f"Weather: {data['weather'][0]['main']} - {data['weather'][0]['description']} - {data['weather'][0]['icon']}")                   # [0] is used to access the first element of the weather list, which contains the weather description.
    print(f"Temp: {data['main']['temp']} C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind: {data['wind']['speed']} m/s")
else:
    print("City Name is Incorrect or API Key Is invalid.")
