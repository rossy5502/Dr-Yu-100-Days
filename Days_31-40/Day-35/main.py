import json
import datetime
def load_weather_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON file.")
        return None

# Load and test the JSON data
if __name__ == "__main__":
    json_file = "rain.json"
    weather_data = load_weather_data(json_file)
    
    if weather_data:
        # Print basic information to verify the data
        print("Successfully loaded weather data:")
        print(f"Location: {weather_data['latitude']}°N, {weather_data['longitude']}°E")
        print(f"Timezone: {weather_data['timezone']} ({weather_data['timezone_abbreviation']})")
        
        # Check for rain alerts
        print("\nChecking for rain alerts:")
        alert_triggered = False
        
        for i in range(len(weather_data['hourly']['time'])):
            time = weather_data['hourly']['time'][i][11:]
            temp = weather_data['hourly']['temperature_2m'][i]
            precip = weather_data['hourly']['precipitation'][i]
            precip_prob = weather_data['hourly']['precipitation_probability'][i]
            
            if precip_prob > 40 and not alert_triggered:
                print("\n🌧️ Rain Alert! 🌧️")
                alert_triggered = True
                
            if precip_prob:
                print(f"{time}: {temp}°C, Precipitation: {precip}mm ({precip_prob}% chance)")
        
