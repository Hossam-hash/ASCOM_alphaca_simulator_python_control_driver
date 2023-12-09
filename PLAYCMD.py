import requests
from ASCOM_functions_Dome import *
#url = 'http://localhost:11000/get_dome/'


def modify_parameter(base_url,basic_,parameter_name, parameter_value):
    # Fetch current data from the server
    response = requests.get(f'{base_url}/get_dome')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data from the response
        json_data = response.json()

        # Modify the specified parameter to the provided value
        json_data["data"][parameter_name] = parameter_value

        # Make a POST request to update the server with the modified data
        response = requests.post(f'{base_url}/get_dome', json=json_data)

        # Print the response from the server
        print(response.text)
    else:
        print(f"Failed to fetch data from {base_url}. Status code: {response.status_code}")
