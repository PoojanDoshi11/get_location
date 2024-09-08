from flask import Flask, render_template, request
import folium
from datetime import datetime
import requests

app = Flask(__name__)

def get_ip_location():
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
        from geopy.geocoders import Nominatim
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def location():
    try:
        # Get IP-based location data
        location_data = get_ip_location()
        lat = float(location_data['latitude'])
        lon = float(location_data['longitude'])

        # Debug: Print the coordinates to ensure they are being received
        print(f"Received Latitude: {lat}, Longitude: {lon}")

        # Create a map centered on the obtained location
        map_obj = folium.Map(location=[lat, lon], zoom_start=15)
        folium.Marker([lat, lon], tooltip='Laptop Location').add_to(map_obj)

        # Save the map as an HTML file with a unique filename
        map_filename = f'static/map_{datetime.now().strftime("%Y%m%d%H%M%S")}.html'
        map_obj.save(map_filename)

        # Debug: Confirm map was saved
        print(f"Map generated and saved as {map_filename}.")

        return render_template('map_view.html', map_filename=map_filename, location_data=location_data)

    except Exception as e:
        # Debug: Print any errors that occur
        print(f"Error: {e}")
        return "Failed to generate map.", 500

if __name__ == "__main__":
    app.run(debug=True)

