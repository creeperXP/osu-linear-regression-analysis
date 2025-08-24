import requests
import csv

# Set your parameters
user = '36585461'
mode = 0 # standard
userMode = 'id'
from_date = '2024-05-01'
to_date = '2025-08-25'

# Build URL
url = f'https://osutrack-api.ameo.dev/hiscores?user={user}&mode={mode}&from={from_date}&to={to_date}&userMode={userMode}'

# Make the request
response = requests.get(url)
data = response.json()

# Save to CSV
with open('hiscores.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("CSV file saved as hiscores.csv")


