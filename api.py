import requests
 
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")  
magnitude = input("Enter minimum magnitude: ")
 
earth_quake = requests.get(f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_date}&endtime={end_date}&minmagnitude={magnitude}")
data = earth_quake.json()  
 
for feature in data['features']:    
    print(f"Magnitude: {feature['properties']['mag']}, Location: {feature['properties']['place']}")
 