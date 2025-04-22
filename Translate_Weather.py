import requests
import time

def get_language():
    """
    Asks the user for their preferred language.

    Returns:   
        str: The user's preferred language ('en', 'es', or 'la').
    """
    while True:
        lang = input("Choose your language (en/es/la): ").strip().lower()
        if lang in ['en', 'es', 'la']:
            return lang
        print("Invalid choice. Please enter 'en' for English, 'es' for Spanish, or 'la' for Latin.")

def get_language_specific_functions(lang):
    """
    Returns language-specific functions for weather and wind speed.

    Args:
        lang (str): The user's preferred language ('en', 'es', or 'la').

    Returns:
        tuple: A tuple containing the language-specific functions.
    """
    if lang == 'en':
        def get_weather(location):
            url = f"https://wttr.in/{location}?format=%C+%t"
            response = requests.get(url)
            if response.status_code == 200:
                return response.text.strip()
            return "Error: Unable to fetch weather data."

        def get_wind_speed(location):
            url = f"https://wttr.in/{location}?format=%w"
            response = requests.get(url)
            if response.status_code == 200:
                return response.text.strip()
            return "Error: Unable to fetch wind speed."

        return get_weather, get_wind_speed

    elif lang == 'es':
        def get_weather(location):
            url = f"https://wttr.in/{location}?format=%C+%t"
            response = requests.get(url)
            if response.status_code == 200:
                return response.text.strip()
            return "Error: No se puede obtener los datos del clima."

        def get_wind_speed(location):
            url = f"https://wttr.in/{location}?format=%w"
            response = requests.get(url)
            if response.status_code == 200:
                return response.text.strip()
            return "Error: No se puede obtener la velocidad del viento."

        return get_weather, get_wind_speed

    elif lang == 'la':
        def get_weather(location):
            url = f"https://wttr.in/{location}?format=%C+%t"
            response = requests.get(url)
            if response.status_code == 200:
                return response.text.strip()
            return "Error: Non potest notitias tempestatum accipere."

        def get_wind_speed(location):
            url = f"https://wttr.in/{location}?format=%w"
            response = requests.get(url)
            if response.status_code == 200:
                return response.text.strip()
            return "Error: Non potest velocitatem venti accipere."

        return get_weather, get_wind_speed

def get_current_time():
    """
    Returns the current time in HH:MM:SS format.
    """ 
    return time.strftime("%H:%M:%S", time.localtime())

# Main script execution
# Ask for language preference
language = get_language()

# Get language-specific functions
get_weather, get_wind_speed = get_language_specific_functions(language)

# Ask for user location
user_location = input("Enter a location: " if language == 'en' else "Ingrese una ubicación: " if language == 'es' else "Intra locum: ")
print("Your location is:" if language == 'en' else "Su ubicación es:" if language == 'es' else "Locus tuus est:", user_location)

# Fetch and display weather information
weather = get_weather(user_location)
print(f"The weather in {user_location} is: {weather}" if language == 'en' else f"El clima en {user_location} es: {weather}" if language == 'es' else f"Tempestas in {user_location} est: {weather}")

# Fetch and display wind speed information
wind_speed = get_wind_speed(user_location)
print(f"The wind speed in {user_location} is: {wind_speed}" if language == 'en' else f"La velocidad del viento en {user_location} es: {wind_speed}" if language == 'es' else f"Velocitas venti in {user_location} est: {wind_speed}")
print("Local Time:", get_current_time())
