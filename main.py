import time
# import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

USERNAME = "x"
PASSWORD = "x"

chrome_driver_path = Service("C:/Users/BC/Development/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&"
           "location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# SIGN IN
sign_in = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/a[1]'))).click()
# driver.find_element(By.XPATH, '/html/body/div[5]/a[1]')
sign_in_page = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
sign_in_page.find_element(By.XPATH, '//*[@id="username"]').send_keys(USERNAME)
sign_in_page.find_element(By.XPATH, '//*[@id="password"]').send_keys(PASSWORD)
sign_in_page.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()

# SELECT JOB
time.sleep(2)
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'scaffold-layout__list-item')))
job_list = driver.find_elements(By.CLASS_NAME, 'job-card-container--clickable')  # 25 jobs per page

for job in job_list:
    try:
        actions = ActionChains(driver)
        actions.move_to_element(job).perform()
        time.sleep(0.2)
        job.click()  # WebDriverWait(job, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'job-card-list__title')))
    except NoSuchElementException:
        print("Job not found")
    else:
        # SAVING
        saving = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(driver.find_element(
            By.CLASS_NAME, 'jobs-save-button')))
        saving.click()  # SAVE JOB LISTING
        time.sleep(0.2)
        saving.click()  # UN-SAVE JOB LISTING

        # FOLLOWING COMP
        follow = driver.find_element(By.CSS_SELECTOR, '.artdeco-button__icon')
        actions.move_to_element(follow).perform()
        follow.click()  # FOLLOW COMPANY
        time.sleep(0.2)
        follow.click()  # UNFOLLOW COMPANY
