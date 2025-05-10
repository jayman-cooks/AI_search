from random import choices
from site_scrape import get_links_from_google, get_website_content

import requests
import re

def parse_single_quote_string(input_string):
    # This regex finds all substrings enclosed in single quotes
    return re.findall(r"'(.*?)'", input_string)

#links = get_links_from_google("stack+overflow+how+to+add+7+strings")
def parse_numbers(s):
    return [float(x.strip()) for x in s.split(',')]

def sanitize_links(links):
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
    return links
def assign_value(query, content):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "messages": [
            {"role": "user",
             "content": f"rank the relevance and originality on a scale of one to ten of this website's content to the query: {query}. Please only respond with your rankings, with relevance first and originality second, separated by a comma. Website content: {content}"}
        ]
    }
    response = requests.post("https://ai.hackclub.com/chat/completions", headers=headers, json=data)
    response_json = response.json()

    # Extract the assistant's message content
    rsp = response_json["choices"][0]["message"]["content"]
    scores = parse_numbers(rsp)
    f_score = scores[0] + scores[1] * 0.5
    return f_score
