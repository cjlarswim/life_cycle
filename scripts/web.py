from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import json


time.sleep(100)
dataold = 0
driver = webdriver.Firefox()
driver.get("file:///home/pi/restart.html")
driver.maximize_window()


while True:
    with open('/home/pi/odcscript/refresh.json') as json_file:
        data = json.load(json_file)
        refresh = data["refresh"]
        print(data)
        print(refresh)

    if dataold == refresh:
        print("No Change")
    else:        
        if refresh == 0:
            driver.get("file:///home/pi/restart.html")
            dataold = 0
        if refresh == 1:
            driver.get("http://192.168.0.102:8080")
            dataold = 1
    time.sleep(10)


#driver.get("https://www.google.de")
#time.sleep(10)



#driver.get("file:///home/pi/restart.html")
#time.sleep(10)
#driver.refresh()
#time.sleep(10)
#driver.close()
