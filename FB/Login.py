from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\shruti\\Desktop\\workspace\\python_tutorial\\FB\\Drivers\\chromedriver.exe")
#time.sleep("3")

driver.set_page_load_timeout("10")

driver.get("https://www.cricbuzz.com/")



#driver.find_element_by_name("email").send_keys("rahul27.shahare@gmail.com")
#driver.find_element_by_name("pass").send_keys("2kl04ee022")
#driver.find_element_by_id("loginbutton").click()



#driver.find_element_by_class_name("_42ft _4jy0 _62c3 _4jy4 _517h _51sy").click()

#time.sleep("10")