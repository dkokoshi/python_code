import requests

# 1. Update these variables with your device's exact details
DEVICE_IP = "192.168.22.1"
USERNAME = "user1"
PASSWORD = "user1"

# 2. Define the target endpoint
# (The exact URL path depends on the device firmware, e.g., /api/system/version or /cgi-bin/version)
URL = f"http://{DEVICE_IP}/api/system/version"

def get_device_version():
    try:
        # Send an HTTP GET request with Digest or Basic Authentication
        response = requests.get(
            URL, 
            auth=(USERNAME, PASSWORD), 
            timeout=10
        )
        
        # Raise an exception for HTTP errors (e.g., 401 Unauthorized, 404 Not Found)
        response.raise_for_status()

        # Print the response (Assuming the device returns JSON)
        data = response.json()
        print("Device Version Info:")
        print(f"Hardware Version: {data.get('hardware_version')}")
        print(f"Firmware Version: {data.get('firmware_version')}")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting to Device: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")

if __name__ == "__main__":
    get_device_version()