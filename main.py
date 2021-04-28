import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


WEBDRV_PATH  = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(WEBDRV_PATH)
action = ActionChains(driver)

#login
driver.get('https://indy.sz-ybbs.ac.at/pages/loginLogout/login.php')
login_un = driver.find_element_by_id('loginWidget.idusername') #finds login username field 
login_un.send_keys('jonas.wahringer') #enter the username
login_password = driver.find_element_by_id('loginWidget.idpassword') #finds pw field
login_password.send_keys('Jy33LfOo') #enters pw
driver.find_element_by_id('loginSubmit').click()

#warten und auf tag klicken
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="calendar"]/div[3]/div[5]')))
search = driver.find_element_by_xpath('//*[@id="calendar"]/div[3]/div[5]')
search.click()

#Stunde eintragen
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="myModal"]/div/div/div[2]/div/div[2]/div[1]/label[1]')))
search = driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[2]/div[1]/label[1]')
search.click()
search = driver.find_element_by_xpath('//*[@id="Lehrerbox"]')
search.click()
search.send_keys("HÖ")
search.send_keys(Keys.ENTER)
search = driver.find_element_by_xpath('//*[@id="Activity"]')
search.send_keys("Mathematik Hausübung")
search = driver.find_element_by_xpath('//*[@id="saveModalSaveButton"]')
search.click()
'''
#Tag aufrufen & #3. Stunde eintragen
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="calendar"]/div[3]/div[5]')))
search = driver.find_element_by_xpath('//*[@id="calendar"]/div[3]/div[5]')
search.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="myModal"]/div/div/div[2]/div/div[2]/div[1]/label[1]')))
search = driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[2]/div[1]/label[1]')
search.click()
search = driver.find_element_by_xpath('//*[@id="Lehrerbox"]')
search.click()
search.send_keys("HÖ")
search.send_keys(Keys.ENTER)
#Tag aufrufen & #4. Stunde eintragen    
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="calendar"]/div[3]/div[5]')))
search = driver.find_element_by_xpath('//*[@id="calendar"]/div[3]/div[5]')
search.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="myModal"]/div/div/div[2]/div/div[2]/div[1]/label[2]')))
search = driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[2]/div[1]/label[]')
search.click()
search = driver.find_element_by_xpath('//*[@id="Lehrerbox"]')
search.click()
search.send_keys("HÖ")
search.send_keys(Keys.ENTER)
'''







'''
#URL = 'https://indy.sz-ybbs.ac.at/pages/loginLogout/login.php'
#USERNAME = 'jonas.wahringer'
#PASSWORD = 'Jy33LfOo'
cookies = {
    'PHPSESSID': 'lksu5m7i0ri29oqur7nkgh62g6',
}
headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://indy.sz-ybbs.ac.at',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://indy.sz-ybbs.ac.at/pages/calendarStudent/calendar.php',
    'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
}
data = [
  ('day', 'Mi^'),
  ('totalHours', '2^'),
  ('date', '2020-12-02^'),
  ('specificHours^%^5B^%^5D', '3^'),
  ('specificHours^%^5B^%^5D', '4'),
]
def main():
    response = requests.post('https://indy.sz-ybbs.ac.at/php/queries/get/loadAll.php', headers=headers, cookies=cookies, data=data)
    json_data= response.json()
    #print(json_data)
    teachers = json_data['teachers']
    subjects = json_data['subjects']
    soup = BeautifulSoup(teachers, 'html.parser')
    print(soup)
if __name__ == '__main__':
    main()
'''


#def get_json_data():
#    response = requests.post('https://indy.sz-ybbs.ac.at/php/queries/get/loadAll.php', headers=headers, cookies=cookies, data=data)
#    json_data= response.json()

#    return json_data

