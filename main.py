from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://weworkremotely.com/")

time.sleep(10)  

def ext_jobs():
    jobs = []
    container = driver.find_element(By.CLASS_NAME, "search-listings__container")  
    sections = container.find_elements(By.CLASS_NAME, "jobs")

    for section in sections:
        listings = section.find_elements(By.CSS_SELECTOR, "li.new-listing-container")

        for li in listings:
            try:
                title_elem = li.find_element(By.CLASS_NAME, "new-listing__header__title")
                company_elem = li.find_element(By.CLASS_NAME, "new-listing__company-name")
                # location_elem = li.find_element(By.CLASS_NAME, "new-listing__company-headquarters")
                category_elems = li.find_elements(By.CSS_SELECTOR, "div.new-listing__categories > p")

                title = title_elem.text.strip()
                company = company_elem.text.strip()
                # location = location_elem.text.strip()
                categories = [cat.text.strip() for cat in category_elems]

                job = {
                    "title": title,
                    "company": company,
                    # "location": location,
                    "categories": categories
                }

                jobs.append(job)

            except Exception as e:
                continue  

    return jobs

if __name__ == "__main__":
    jobs = ext_jobs()
    for i, job in enumerate(jobs, 1):
        print(f"{i}. {job['title']}")
        print(f"   Company: {job['company']}")
        print(f"   Tags: {', '.join(job['categories'])}")
        print("--------")
