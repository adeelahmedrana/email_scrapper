from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

def main():
    base_url = "http://www.cityoflondonschool.org.uk"
    # We'll look for "Contact us" link and then go there.

    # 1) Set up headless Chrome (invisible browser)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # 2) Load the base page
    driver.get(base_url)
    # Wait a moment for JavaScript to load menus
    time.sleep(3)

    # 3) Find the "contact us" link
    contact_link = None
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        text = link.text.strip().lower()
        href = link.get_attribute("href")
        # If "contact" in text or href, store it
        if href and "contact" in href.lower():
            contact_link = href
            break
        elif "contact" in text:
            contact_link = href
            break

    if contact_link:
        print(f"Found contact page link: {contact_link}")
    else:
        print("No 'contact us' link found via Selenium.")
        driver.quit()
        return

    # 4) Navigate to the contact page
    driver.get(contact_link)
    time.sleep(2)  # wait for the contact page to render

    # 5) Extract emails from page source with a simple regex
    page_html = driver.page_source
    emails = re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", page_html)
    unique_emails = set(emails)

    if unique_emails:
        print("Emails found on the contact page:")
        for email in unique_emails:
            print(" -", email)
    else:
        print("No emails found on the contact page.")

    # 6) Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
