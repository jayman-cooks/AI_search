from random import choices
from site_scrape import get_links_from_google, get_website_content

import requests
import re

def parse_single_quote_string(input_string):
    # This regex finds all substrings enclosed in single quotes
    return re.findall(r"'(.*?)'", input_string)
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
links = parse_single_quote_string(content)
print(links)
content_url = {}
for i in links:
    content = get_website_content(i)
    print(f"got content of {i}")
    content_url.update({url: content})
