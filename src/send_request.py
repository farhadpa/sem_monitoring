import json
import requests
from alert import send_email

# function to send request to the service and act accordingly
def send_request(url, payload, result):
    try:
        # Make a GET request to the service's endpoint
        response = requests.post(url, json=payload)
        # Check the status code of the response
        if response.status_code == 200:
            # Parse and process data received
            data = response.text
            # result is what we expect to receive(from test_data.py)
            if (json.loads(data)) == result:
                # this logs the result to the terminal
                print(data) 
            else:
                print(f"Error: Received unexpected result {data} from service {payload['action']}")
                send_email(f"Error: Received unexpected result {data} from service {payload['action']}")
        else:
            print(f"Error: Received status code {response.status_code}")
            send_email(f"Error: Received status code {response.status_code} from service {payload['action']}")
    except requests.RequestException as e:
        print(f"Error: {e}")
        send_email(f"Error: {e} from service {payload['action']}")
    
