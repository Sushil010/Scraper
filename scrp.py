
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# driver.get("https://weworkremotely.com/")
# wait = WebDriverWait(driver, 10)

# time.sleep(10)  

# def ext_jobs():
#     jobs=[]
#     container=driver.find_element(By.CLASS_NAME,"search-listings__container")
#     section=container.find_elements(By.CLASS_NAME,"jobs")

#     for job in section:
#         title=job.find_elements(By.CLASS_NAME,"new-listing__header__title")
#         try:
#             print(title)
#         except Exception:
#             continue
# ext_jobs()



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://weworkremotely.com/")

time.sleep(10)  # let the page load

def ext_jobs():
    jobs = []
    container = driver.find_element(By.CLASS_NAME, "search-listings__container")  # fixed class name
    sections = container.find_elements(By.CLASS_NAME, "jobs")

    for section in sections:
        listings = section.find_elements(By.CSS_SELECTOR, "li.new-listing-container")

        for li in listings:
            try:
                title_elem = li.find_element(By.CLASS_NAME, "new-listing__header__title")
                company_elem = li.find_element(By.CLASS_NAME, "new-listing__company-name")
                location_elem = li.find_element(By.CLASS_NAME, "new-listing__company-headquarters")
                category_elems = li.find_elements(By.CSS_SELECTOR, "div.new-listing__categories > p")

                title = title_elem.text.strip()
                company = company_elem.text.strip()
                location = location_elem.text.strip()
                categories = [cat.text.strip() for cat in category_elems]

                job = {
                    "title": title,
                    "company": company,
                    "location": location,
                    "categories": categories
                }

                jobs.append(job)

            except Exception as e:
                continue  # skip if any element is missing

    return jobs

# Run and print
job_list = ext_jobs()
for i, job in enumerate(job_list, 1):
    print(f"{i}. {job['title']}")
    print(f"   Company: {job['company']}")
    print(f"   Location: {job['location']}")
    print(f"   Tags: {', '.join(job['categories'])}")
    print("--------")
