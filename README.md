# timezone-conversion-tool
This Python tool allows users to easily convert time between different time zones. Given a target time in one city, the program calculates the corresponding time in another city, taking into account the differences in time zones

## Features
- Dynamic Time Zone Detection: Utilizes geolocation and public APIs to dynamically determine time zones based on city names or coordinates.
- Intuitive Input: Accepts user-friendly input for city names and target times, making it accessible for users.
- Accurate Time Calculations: Calculates accurate time conversions, considering the specific target time and respective time zones.
## Usage
- Provide the names of the current city, target city, and target time.
- The program fetches coordinates and time zone information for the specified cities.
- It calculates the future time in the current city when it's the specified time in the target city.
- Outputs the result in a clear and readable format.
## How to Run
- Clone the repository.
- Install the necessary Python libraries: geopy, pytz, and timezonefinder.
- Run the Python script and follow the prompts to input the required information.
## Dependencies
- geopy: A Python library for geocoding (finding latitude and longitude of addresses).
- pytz: A Python library for working with time zones.
- timezonefinder: A Python library for finding time zones based on coordinates.
