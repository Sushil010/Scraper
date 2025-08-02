# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # import time

# # service = Service(executable_path="chromedriver.exe")
# # driver = webdriver.Chrome(service=service)

# # driver.get("https://weworkremotely.com/")
# # time.sleep(10)  # give time for the page to load

# # # find all job listings
# # job_listings = driver.find_elements(By.CLASS_NAME, "new-listing-container")
# # print(f"Found {len(job_listings)} jobs")

# # # extract links or titles
# # for job in job_listings:
# #     try:
# #         link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
# #         company_name=job.find_element(By.CLASS_NAME,"new-listing__categories")
# #         # print(company_name)
# #         if(len(company_name)>=3):
# #             work_time=company_name[0].text
# #             salary=company_name[1].text
# #             location=company_name[2].text
# #             print(f"{link}-{work_time}-{salary}-{location}")
# #         # print(link)
# #     except:
# #         continue

# # driver.quit()



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# driver.get("https://weworkremotely.com/")
# time.sleep(10)  # you don't need 60 seconds

# job_listings = driver.find_elements(By.CLASS_NAME, "new-listing-container")
# print(f"Found {len(job_listings)} jobs")

# for job in job_listings:
#     try:
#         title=job.find_element(By.CLASS_NAME,"new-listing__header__title")
#         company=job.find_element(By.CLASS_NAME,"new-listing__company-name")
#         link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
#         categories = job.find_elements(By.CLASS_NAME, "new-listing__categories__category")
#         if len(categories) >= 3:
#             work_time = categories[0].text
#             salary = categories[1].text
#             location = categories[2].text
#             print(f"{link} - Title:{title.text} - Time:{work_time} - Name:{company.text} - Salary:{salary} - Location: {location}")
        
#     except Exception as e:
#         continue

# driver.quit()




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://weworkremotely.com/")
wait = WebDriverWait(driver, 10)

time.sleep(10)  

def extract_jobs():
    jobs = []
    job_listings = driver.find_elements(By.CLASS_NAME, "new-listing-container")
    for job in job_listings:
        try:
            title = job.find_element(By.CLASS_NAME, "new-listing__header__title").text
            company = job.find_element(By.CLASS_NAME, "new-listing__company-name").text
            link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
            categories = job.find_elements(By.CLASS_NAME, "new-listing__categories__category")
            if len(categories) >= 3:
                work_time = categories[0].text
                salary = categories[1].text
                location = categories[2].text
                jobs.append({
                    'link': link,
                    'title': title,
                    'company': company,
                    'work_time': work_time,
                    'salary': salary,
                    'location': location
                })
        except Exception:
            continue
    return jobs

all_jobs = extract_jobs()
print(f"Found {len(all_jobs)} jobs before clicking View All")

try:
    view_all_button = driver.find_element(By.LINK_TEXT, "View all")
    actions = ActionChains(driver)
    actions.move_to_element(view_all_button).perform()  
    time.sleep(2)
    view_all_button.click()
    print("Clicked View All button")

   
    time.sleep(20)
    more_jobs = extract_jobs()
    print(f"Found {len(more_jobs)} jobs after clicking View All")

    all_jobs = more_jobs  

except Exception as e:
    print("View All button not found or error:", e)

for job in all_jobs:
    print(job)

driver.quit()
