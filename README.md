# Fanciest Weather App

A simple yet fancy command-line weather application that provides current temperature information for any location worldwide.

## Features

- Get current temperature for any location
- Support for detailed location input (including zip codes, country, state, or complete addresses)
- Display temperature in both Celsius and Fahrenheit
- Clean and formatted location output

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository
2. Install the required dependencies:
```bash
pip install requests
```
## Usage

Run the script:
```shell script
python weather.py
```


The application will:
1. Prompt you to enter a location
2. Display the current temperature in both Celsius and Fahrenheit
3. Show a formatted version of the location

## APIs Used

- [Open-Meteo API](https://open-meteo.com/) - For weather data
- [Geoapify API](https://www.geoapify.com/) - For geocoding services

## Example Output
```
*** THE MOST FANCY WEATHER APP EVER ***
***************************************
Please enter a location: New York
The current temperature in New York, USA, is 20°C/68.0°F
Not the location you meant? Start over and add details like zip code, country or state. You can even enter a complete address.
************** GOOD BYE  **************
```


## Note

Make sure you have an active internet connection as the application requires access to external APIs for weather and location data.

## License

This project is open source and available under the MIT License.

