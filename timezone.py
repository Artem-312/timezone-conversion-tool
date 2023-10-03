import pytz
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder


def get_timezone_from_coordinates(latitude, longitude):
    tz_finder = TimezoneFinder()
    timezone_str = tz_finder.timezone_at(lat=latitude, lng=longitude)
    return pytz.timezone(timezone_str) if timezone_str else None


def calculate_future_time(target_time, target_timezone, target_datetime):
    target_time_parts = target_time.split(':')
    target_hour = int(target_time_parts[0])
    target_minute = int(target_time_parts[1])

    # Create a datetime object for the target time in the target timezone
    target_datetime = target_datetime.replace(hour=target_hour, minute=target_minute)

    # Convert the target time to the target timezone
    target_datetime = target_timezone.localize(target_datetime)

    return target_datetime


if __name__ == "__main__":
    while True:
        # Get user input for the current city, target city, and target time
        current_city = input("Enter your current city: ")
        target_city = input("Enter your target city: ")
        target_time = input("Enter your tarhet time (HH:MM): ")

        # Get coordinates for the cities
        geolocator = Nominatim(user_agent="timezone_converter")
        current_location = geolocator.geocode(current_city)
        target_location = geolocator.geocode(target_city)

        if current_location and target_location:
            try:
                # Determine the time zone for the target city
                target_timezone = get_timezone_from_coordinates(target_location.latitude, target_location.longitude)

                # Get the current datetime
                current_datetime = datetime.now()

                # Calculate the future time in the target city
                target_datetime = calculate_future_time(target_time, target_timezone, current_datetime)

                # Determine the time zone for the current city
                current_timezone = get_timezone_from_coordinates(current_location.latitude, current_location.longitude)

                # Convert the future time from the target city to the current city
                current_time = target_datetime.astimezone(current_timezone)

                print(
                    f"Time in {current_city} when it is {target_time} in {target_city} is {current_time.strftime('%H:%M')}.")
                print("")
            except Exception as e:
                print(f"Error: {str(e)}")
        else:
            print("Error when getting coordinates of one or both cities.")
