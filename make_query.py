from site_scrape import get_links_from_google, get_website_content
from chat_completions import sanitize_links, assign_value

def make_query(query):
    # formats the query for google
    g_query = query.replace(" ", "+")
    urls_content = get_website_content(sanitize_links(get_links_from_google(g_query)))

    processed = {key: assign_value(query, val) for key, val in urls_content.items()}

    # Sort keys based on processed values in descending order
    ranked_keys = sorted(processed, key=processed.get, reverse=False)

    print(urls_content)
    print(ranked_keys)
    return ranked_keys
