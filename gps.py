from geopy.geocoders import Nominatim
import requests

def get_location():
    try:
        # Get public IP address
        ip_request = requests.get('https://api.ipify.org?format=json')
        ip_address = ip_request.json()['ip']

        # Get location details based on IP address
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        location_data = response.json()

        # Extract latitude and longitude
        loc = location_data['loc'].split(',')
        latitude, longitude = loc[0], loc[1]

        # Use geopy to get a more readable address
        geolocator = Nominatim(user_agent="my_app_name_contact@example.com")
        location = geolocator.reverse(f"{latitude}, {longitude}")

        return {
            'ip': ip_address,
            'latitude': latitude,
            'longitude': longitude,
            'address': location.address if location else "Address not found"
        }

    except Exception as e:
        print(f"Error retrieving location: {e}")
        return {
            'ip': 'Unknown',
            'latitude': 'Unknown',
            'longitude': 'Unknown',
            'address': 'Error retrieving address'
        }

# Fetch and print location for debugging
location = get_location()
print(f"IP: {location['ip']}")
print(f"Latitude: {location['latitude']}")
print(f"Longitude: {location['longitude']}")
print(f"Address: {location['address']}")

