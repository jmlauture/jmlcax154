# GPS Coordinator tracker for drone
#
destination = (34.0522, -118.2437)  # Example GPS coordinates (latitude, longitude)
def update_drone_location(new_location):
    global destination  # Use the global variable to update the location
    destination = new_location
    print(f"Drone location updated to: {destination}")   
# Example usage

# new_location = (34.1111, -122.0524)  # New GPS coordinates (latitude, longitude)
new_location = input("Enter new drone location (latitude, longitude) separated by a comma: ")
new_location = tuple(map(float, new_location.split(',')))  # Convert input string to a tuple of floats
update_drone_location(new_location) 

print("Tracking drone location...")
print(f"Current Destination Latitude: {destination[0]}")
loc_latitude = destination[0]
loc_longitude = destination[1]  
print(f"Current Drone Location: Latitude: {loc_latitude}, Longitude: {loc_longitude}")
