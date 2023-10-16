from selenium import webdriver
from selenium.webdriver.common.by import By

# driver_path = r'C:\Users\az294\AppData\Local\Programs\Python\Python37\chromedriver.exe'
driver = webdriver.Chrome()
#  访问指定的url:url必须要带有http://的字样。
driver.get("https://www.baidu.com/")
# driver.find_element(By.ID, 'kw').send_keys("自动化测试")
# driver.find_elementBy.ID, 'su').click()

