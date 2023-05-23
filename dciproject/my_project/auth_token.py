import requests

# Set the token value
token = '06f32d9c09c66a9942a95c2b0f08db3b96dbf58f'

# Set the API endpoint URL
url = 'http://127.0.0.1:8000/'

# Set the headers with the Authorization token
headers = {
    'Authorization': f'Token {token}'
}

# Send a GET request with authentication
response = requests.get(url, headers=headers)

# Process the response
print(response.status_code)
print(response.json())
