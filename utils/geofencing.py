import math

def is_within_boundary(student_lat, student_lon, school_lat, school_lon, max_distance_km):
    """
    Determine whether a student is within the allowed geographical boundary.

    Parameters:
        student_lat (float): Student's current latitude
        student_lon (float): Student's current longitude
        school_lat (float): School's latitude
        school_lon (float): School's longitude
        max_distance_km (float): Maximum allowed distance in kilometers

    Returns:
        bool: True if student is within the allowed boundary, False otherwise
    """

    EARTH_RADIUS_KM = 6371

    delta_lat = math.radians(school_lat - student_lat)
    delta_lon = math.radians(school_lon - student_lon)

    student_lat_rad = math.radians(student_lat)
    school_lat_rad = math.radians(school_lat)

    a = (math.sin(delta_lat / 2) ** 2 +
         math.cos(student_lat_rad) *
         math.cos(school_lat_rad) *
         math.sin(delta_lon / 2) ** 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = EARTH_RADIUS_KM * c

    return distance <= max_distance_km