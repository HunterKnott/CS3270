import reverse_geocoder
import indexer

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

def get_location(dd):
    return reverse_geocoder.search(dd)

def format_location(location):
    output = f"{location[0]['name']}, {location[0]['admin1']} {location[0]['cc']}"
    return output

if __name__ == "__main__":
    lat = "[44, 8, 307/100]"
    lat_ref = "N"
    long = "[124, 7, 121/5]"
    long_ref = "W"
    lat_dd = process_coord(lat, lat_ref)
    long_dd = process_coord(long, long_ref)
    loc = get_location((lat_dd, long_dd))
    format_location(loc)