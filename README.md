# Location-Based Map Viewer

A Flask web application that detects the user's geographical location based on their public IP address and displays it on an interactive map using Folium. The app fetches location details such as latitude, longitude, and a human-readable address, providing a visual display centered on the user's current location.

## Features

- **IP-based Location Detection**: Automatically retrieves the user's geographical location using their public IP address.
- **Interactive Map**: Displays the user's location on a dynamic map powered by Folium.
- **Location Information**: Shows precise details like latitude, longitude, and an approximate address (with a possible margin of error up to 5 km).

## Project Structure

- `app.py`: The main Flask application that runs the web server and generates the location-based map.
- `gps.py`: A helper script for fetching and printing the user’s location (IP-based) for debugging purposes.
- `templates/`: Contains the HTML files used to render the front end.
- `static/`: A directory reserved for static files (e.g., images, saved locations, CSS files) that can be used in future projects.

## Requirements

- **Git**: Version control system to clone the repository.
- **Python 3.x**: Required for running the application.
- **Pip**: Python's package manager to install dependencies.

## Installation Instructions

### 0. Make venv (not mendatory but suggestable for handling the versions)

#### For Linux/macOS
``` bash
python3 -m venv venv
source venv/bin/activate
```
#### For windows
``` bash
python -m venv venv
.\venv\Scripts\activate
```

### 1. Clone the Repository

```bash
git clone https://github.com/PoojanDoshi11/get_location.git
cd get_location
pip install -r requirements.txt
```
### 2. Run Application

#### For Linux/macOS
``` bash
python3 app.py
```
#### For windows
``` bash
python app.py
```
- Open your browser and navigate to http://127.0.0.1:5000/ to view the interactive map showing your location.

## Notes

### 1. Location Accuracy:
- The IP-based location detection relies on third-party services, which may not provide accurate geolocation. The results can vary by up to 5 km, especially if you are using a VPN or proxy.

### 2. No Internet Connection:
- If the application fails to retrieve your IP-based location, make sure you have an active internet connection. The app queries external geolocation services that require internet access.

### 3. Firewall or Network Restrictions:
- Some corporate or secured networks might block access to geolocation APIs, leading to errors in retrieving location data. In this case, try running the app on a different network or contact the network administrator to whitelist the necessary services.

### 4. Missing Dependencies:
- If requirements.txt is missing or incomplete, you might encounter errors related to missing Python packages. Ensure that all dependencies are listed and installed correctly with:
  ```bash
   pip install -r requirements.txt
  ```
### 5. Virtual Environment Issues:
- If you encounter issues with missing libraries, ensure that the virtual environment is activated before running the app:
-- Linux/macOS: source venv/bin/activate
-- Windows: .\venv\Scripts\activate





