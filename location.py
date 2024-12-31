import requests

# Function to get location details
def get_location_from_coordinates(api_key, latitude, longitude):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={latitude}+{longitude}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            formatted_address = data['results'][0]['formatted']
            return formatted_address
        else:
            return "Location not found."
    else:
        return f"Error: {response.status_code}"

# Your existing data
latitude = 37.7749  # Replace with your latitude
longitude = -122.4194  # Replace with your longitude
isp = "Your ISP"  # Replace with your ISP (if collected already)
country = "Your Country"  # Replace with your country (if collected already)
currency = "Your Currency"  # Replace with your currency (if collected already)

# Your OpenCageData API Key
api_key = "YOUR_API_KEY"

# Get location
location = get_location_from_coordinates(api_key, latitude, longitude)

# Display the information
print("Latitude:", latitude)
print("Longitude:", longitude)
print("ISP:", isp)
print("Country:", country)
print("Currency:", currency)
print("Location:", location)
