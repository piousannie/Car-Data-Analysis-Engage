import pandas as pd
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
import os
import codecs

#setup driver for scraping
driver = webdriver.Chrome("C:/Users/aulee/Downloads/chromedriver_win32/chromedriver.exe",options=chrome_options)
target_url="https://www.marklines.com/en/members/login"
driver.get(target_url)

#login to target url
username=""
passw=""
login_ID=driver.find_element_by_id("profiles_login_login_id")
login_Pass=driver.find_element_by_id("profiles_login_password")
login=driver.find_element_by_id("login_btn")
login_ID.send_keys(username)
login_ID.send_keys(passw)
login.click()

#launch URL
driver.get("https://www.marklines.com/en/vehicle_preset/search/graph?mode=2&numberCategory=1&isMonthly=false&nationCode=IND&fromYear=2012&toYear=2021")

#get file path to save page
dir_path = os.getcwd()
n=os.path.join(dir_path,"Page.html")
#open file in write mode with encoding
file= codecs.open(n, "w", "utf−8")
#obtain page source
h = driver.page_source
#write page source content to file
file.write(h)
#close browser
driver.quit()

#reading the tables from the source
table_MN = pd.read_html('carspage.html')
print(f'Total tables: {len(table_MN)}')

#saving the tables as CSV
df=table_MN[1]
print(df.head())

df.to_csv("SalesReport.csv")