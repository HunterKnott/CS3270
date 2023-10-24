import reverse_geocoder

# Changes a coordinate string to a list of numeric values
def process_coord(dms, ref):
    values = dms.strip("[]").split(",")
    num_values = []
    for value in values:
        try:
            numeric_value = eval(value)
            num_values.append(numeric_value)
        except:
            print(f"Failed to parse value {value}")

    decimal_degrees = num_values[0] + (num_values[1] / 60) + (num_values[2] / 3600)
    if ref in ["S", "W"]:
        decimal_degrees = -(decimal_degrees)
    
    return decimal_degrees

# Returns coordinates given the a Decimal Degrees numeric value
def get_location(dd):
    return reverse_geocoder.search(dd)

# Returns a city, state/province, and country given coordinates
def format_location(location):
    output = f"{location[0]['name']}, {location[0]['admin1']} {location[0]['cc']}"
    return output

# Takes latitude and longitude information and returns a location
def main(lat_tuple, long_tuple):
    lat_dd = process_coord(lat_tuple[0], lat_tuple[1])
    long_dd = process_coord(long_tuple[0], long_tuple[1])
    loc = get_location((lat_dd, long_dd))
    return format_location(loc)

if __name__ == "__main__":
    main()