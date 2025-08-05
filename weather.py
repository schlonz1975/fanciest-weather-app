import requests
import sys
import os


def main():
    os.system("clear")
    print("*** THE MOST FANCY WEATHER APP EVER ***")
    print("***************************************")
    location = input("Please enter a location: ")
    coords = get_coordinates(location)
    clean_location = get_formatted_location(location)
    longitude = coords[0]
    latitude = coords[1]
    print(
        f"The current temperature in {clean_location}, is {get_temperature(longitude, latitude)} \N{DEGREE SIGN}C/"
        f"{convert_celsius_to_fahrenheit(get_temperature(longitude, latitude)):.1f} \N{DEGREE SIGN}F")
    print("Not the location you meant? Start over and add details like zip code, country or state. You can even "
          "enter a complete address.")
    print("************** GOOD BYE  **************")


# fetching the current temperature from given coordinates
def get_temperature(lon, lat):
    try:
        response = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m")
        content = response.json()
        return content["current"]["temperature_2m"]
    except requests.HTTPError:
        print("Could not complete the request!")
        sys.exit()


# converting the user's location to longitude and latitude for the most relevant result
def get_coordinates(loc):
    try:
        response = requests.get(
            f"https://api.geoapify.com/v1/geocode/search"
            f"?text={loc}&format=json&apiKey=384e4afa88be4f18908923b81fdc2687")
        content = response.json()
        return [content["results"][0]["lon"], content["results"][0]["lat"]]
    except requests.HTTPError:
        print("Could not complete the request!")
        sys.exit()


# formatting the user's location
def get_formatted_location(raw_loc):
    try:
        response = requests.get(
            f"https://api.geoapify.com/v1/geocode/search"
            f"?text={raw_loc}&format=json&apiKey=384e4afa88be4f18908923b81fdc2687")
        content = response.json()
        return content["results"][0]["formatted"]
    except requests.HTTPError:
        print("Could not complete the request!")
        sys.exit()


# converting the temperature to Fahrenheit for US users
def convert_celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


if __name__ == "__main__":
    main()
