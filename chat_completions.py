from random import choices
from site_scrape import get_links_from_google

import requests

links = get_links_from_google("stack+overflow+how+to+add+7+strings")


url = "https://ai.hackclub.com/chat/completions"
headers = {
    "Content-Type": "application/json"
}
data = {
    "messages": [
        {"role": "user", "content": f"take this list and filter it for only reputable sources. Do not add any extra content or commentary; only the list of reputable links will suffice. List: {links}"}
    ]
}

response = requests.post(url, headers=headers, json=data)
response_json = response.json()

# Extract the assistant's message content
content = response_json["choices"][0]["message"]["content"]

print(content)