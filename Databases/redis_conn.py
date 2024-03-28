# Hunter Knott, CS 3530, Utah Valley University
import sys
import redis

def main():
    # Connect to Redis
    client = redis.Redis(host='localhost', port=6379, db=0)
    
    keys = client.keys('*')
    matches = []

    # Search for a contact with provided last name from cli
    if len(sys.argv) > 1:
        for key in keys:
            data = client.lrange(key, 0, -1)
            if data[0].decode() == sys.argv[1]:
                matches.append(data)
    elif len(sys.argv) == 1:
        for key in keys:
            data = client.lrange(key, 0, -1)
            print(data)
        print("No last name provided, all contacts displayed")
    
    print("\nMatches:")
    print(matches)

if __name__ == "__main__":
    main()