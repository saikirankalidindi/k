import requests

url = 'http://localhost:5000/skills'
headers = {'Content-Type': 'application/json'}

data = {
    'skills': 'python'
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
