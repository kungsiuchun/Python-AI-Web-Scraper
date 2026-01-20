import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time


def scrape_webpage(url):
    # Set up the Chrome WebDriver (make sure to have the correct path to your chromedriver)
    print("Launching webdriver")

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to the webpage
        driver.get(url)
        
        print("Page loaded...")
        # Extract the page source
        page_source = driver.page_source
        time.sleep(10)

        return page_source
    finally:
        driver.quit()

def extract_body_content(html):

    print("Extracting body content...")
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.body

    return body.get_text() if body else ''

def clean_body_content(text):

    print("Cleaning body content...")
    soup = BeautifulSoup(text, 'html.parser')

    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()  # Remove these tags

    cleaned_content = soup.get_text(separator='\n')
    cleaned_content = '\n'.join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)
    ]