import requests

location=input("Enter your city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=fb0a521183cf4c889e095848262410&q={location}"

response = requests.get(url)

print(response.status_code)

if response.status_code == 200:
    data = response.json()
    # print(data['current']['temp_c'])
    # print(data['current']['condition']['text'])
    print(f"The weather in{location}, is {data['current']['condition']['text']} with a temperature of {data['current']['temp_c']}°C.")


