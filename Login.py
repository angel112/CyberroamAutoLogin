from selenium import webdriver

driver = webdriver.Chrome(' """Enter path of chromedriver.exe on your disk here""" ')

driver.get('https://172.16.1.1:8090/')

user = "  """Enter Your Username Here"""  "
passw = " """Enter Your Password Here""" "

a = driver.find_element_by_xpath("//input[@type = 'text']")
a.send_keys(user)

b = driver.find_element_by_xpath("//input[@type = 'password']")
b.send_keys(passw)

driver.find_element_by_xpath("//input[@type = 'submit']").click()

driver.close()



                
