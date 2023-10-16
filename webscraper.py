from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time 

df = pd.read_csv('/Users/athulkallungal/Downloads/2023-10-13_-_Worker_and_Temporary_Worker.csv')
company_names = df['Organisation Name'].tolist()

company_sector = []
company_not_sector = []
driver = webdriver.Chrome()
url = "https://find-and-update.company-information.service.gov.uk/"

print(company_names)

for company in company_names:
    driver.get(url)
    input_field = driver.find_element("xpath",'//*[@id="site-search-text"]')
    input_field.clear()
    input_field.send_keys(company)
    driver.find_element("xpath",'//*[@id="search-submit"]').click()
    driver.find_element("xpath",'//*[@id="results"]/li[1]/h3/a').click()
    try:
        span_element = driver.find_element("id","sic0")
        company_sector.append(span_element.text.split('-')[1].strip())
    except:
        company_sector.append("Not Found")
    time.sleep(5)

df['sector'] = company_sector

df.to_csv('/Users/athulkallungal/Downloads/Ukcompaniessponsors.csv',index = False)

