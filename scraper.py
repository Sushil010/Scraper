# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# driver.get("https://weworkremotely.com/")
# time.sleep(10)  # give time for the page to load

# # find all job listings
# job_listings = driver.find_elements(By.CLASS_NAME, "new-listing-container")
# print(f"Found {len(job_listings)} jobs")

# # extract links or titles
# for job in job_listings:
#     try:
#         link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
#         company_name=job.find_element(By.CLASS_NAME,"new-listing__categories")
#         # print(company_name)
#         if(len(company_name)>=3):
#             work_time=company_name[0].text
#             salary=company_name[1].text
#             location=company_name[2].text
#             print(f"{link}-{work_time}-{salary}-{location}")
#         # print(link)
#     except:
#         continue

# driver.quit()



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://weworkremotely.com/")
time.sleep(10)  # you don't need 60 seconds

job_listings = driver.find_elements(By.CLASS_NAME, "new-listing-container")
print(f"Found {len(job_listings)} jobs")

for job in job_listings:
    try:
        title=job.find_element(By.CLASS_NAME,"new-listing__header__title")
        company=job.find_element(By.CLASS_NAME,"new-listing__company-name")
        link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
        categories = job.find_elements(By.CLASS_NAME, "new-listing__categories__category")
        if len(categories) >= 3:
            work_time = categories[0].text
            salary = categories[1].text
            location = categories[2].text
            print(f"{link} - {title.text} - {work_time} - {company.text} - {salary} - {location}")
    except Exception as e:
        continue

driver.quit()

