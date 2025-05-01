from Tools.scripts.linktree import linknames
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile



def get_links_from_google(query="popcorn"):
    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    list_of_links = []
    for x in range(10):
        driver.get(f"https://www.google.com/search?q={query}&start={x}0")


        elements = driver.find_elements(By.PARTIAL_LINK_TEXT, ".")
        for i in elements:
            print("new element")
            print(i.text)
            print("link grabbed:")
            print(i.get_attribute("href"))
            list_of_links.append(i.get_attribute("href"))

    print(f"list: {list_of_links}")
    driver.quit()
    return list_of_links
def get_website_content(url="https://en.wikipedia.org/wiki/Popcorn"):
    options = Options()
    firefox_profile = FirefoxProfile()
    firefox_profile.set_preference("javascript.enabled", False)
    options.profile = firefox_profile

    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(20)
    driver.get(url)
    elements = driver.find_elements(By.TAG_NAME, "p")
    content = []
    for i in elements:
        print(i.text)
        content.append(i.text)
    driver.quit()

print(get_links_from_google("Trump U.N. ambassador"))