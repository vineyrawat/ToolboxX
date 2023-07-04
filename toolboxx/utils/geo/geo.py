import math

def is_user_within_range(latitude_user, longitude_user, latitude_website, longitude_website, radius_limit):
    # Calculate the distance between user and website coordinates using the Haversine formula
    R = 6371  # Earth radius in kilometers

    # Convert latitude and longitude from degrees to radians
    lat_user_rad = math.radians(latitude_user)
    lon_user_rad = math.radians(longitude_user)
    lat_website_rad = math.radians(latitude_website)
    lon_website_rad = math.radians(longitude_website)

    # Calculate the differences between the user and website coordinates
    delta_lat = lat_website_rad - lat_user_rad
    delta_lon = lon_website_rad - lon_user_rad

    # Haversine formula
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat_user_rad) * math.cos(lat_website_rad) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c * 1000  # Convert distance to meters

    # Check if the user is within the radius limit
    if distance <= radius_limit:
        return True
    else:
        return False

def test():
    latitude_user = 28.247095  # Latitude of the user
    longitude_user = 77.346474  # Longitude of the user
    latitude_website = 28.246892  # Latitude of the website
    longitude_website = 77.346834  # Longitude of the website


    can_access = is_user_within_range(latitude_user, longitude_user, latitude_website, longitude_website, 1000)
    if can_access:
        print("User can access the website.")
    else:
        print("User cannot access the website.")
