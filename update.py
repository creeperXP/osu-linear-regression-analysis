import requests
import json

# Parameters
user_id = '36585461'  # Replace with the correct user ID
mode = 0  # 0=osu!, 1=taiko, 2=ctb, 3=mania

# API endpoint
url = f"https://osutrack-api.ameo.dev/update?user={user_id}&mode={mode}"

# Send POST request to update
response = requests.post(url)

# Parse the response JSON
data = response.json()

# Save the full response to a text file
with open('user_update.txt', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=2))

print("Update saved to user_update.txt")



