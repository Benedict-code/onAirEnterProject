import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


#initialization
driver=webdriver.Chrome()

#URL opening and maximize browser window
driver.get("https://lv.sportsdirect.com/")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()

#Item1 search (lonsdale jersey polo shirt mens)
driver.find_element(By.ID, "txtSearch").send_keys("polos")
driver.find_element(By.XPATH, "//span[normalize-space()='Search']").click()
driver.find_element(By.XPATH, "//li[1]//div[1]//div[1]//div[1]//a[1]//div[1]//img[1]").click()
driver.find_element(By.XPATH, "//img[@alt='White/Navy']").click()

#item1 view options
click_next_1=driver.find_element(By.XPATH, "//a[@rel='next']//span")
for i in range(0,4):
    click_next_1.click()
    time.sleep(2)

#item1 size and quantity selection
driver.find_element(By.XPATH, "//div[@id='productVariantAndPrice']//li[1]//a[1]").click()
driver.find_element(By.XPATH, "//span[@class='prodadd']").click()

#item1 add to bad
driver.find_element(By.ID, "aAddToBag").click()
time.sleep(4)

#item2 search (Nike Air Zoom Pegasus)
driver.find_element(By.ID, "txtSearch").send_keys("shoes")
driver.find_element(By.XPATH, "//span[normalize-space()='Search']").click()
driver.find_element(By.XPATH, '//*[@id="navlist"]/li[1]/div/div/div[1]/a[1]/div/img').click()
driver.find_element(By.XPATH, "//img[@alt='Black/Crimson']").click()

#item2 view options
click_next_2=driver.find_element(By.XPATH, "//a[@rel='next']//span")
for i in range(0,7):
    click_next_2.click()
    time.sleep(2)

#item2 size selection and add to bag
driver.find_element(By.XPATH, "//span[normalize-space()='11.5 (47)']").click()
driver.find_element(By.XPATH, "//span[@class='prodadd']").click()
driver.find_element(By.ID, "aAddToBag").click()
time.sleep(2)

#items checkout
bags=driver.find_element(By.ID, "bagQuantityContainer")
action=ActionChains(driver)
action.move_to_element(bags).perform()
driver.find_element(By.XPATH, "//a[@id='aCheckout']//span[contains(text(),'Checkout')]").click()

#customer account login
driver.find_element(By.ID, "Login_EmailAddress").send_keys("testing001@gmail.com")
driver.find_element(By.ID, "Login_Password").send_keys("Testing070")
driver.find_element(By.ID, "LoginButton").click()

#Delivery options
first_name=driver.find_element(By.ID, "NewAddressSelection_Address_FirstName")
first_name.clear()
first_name.send_keys("test")
last_name=driver.find_element(By.ID, "NewAddressSelection_Address_Surname")
last_name.clear()
last_name.send_keys("testing")
adres_1=driver.find_element(By.ID,"NewAddressSelection_Address_Line1")
adres_1.clear()
adres_1.send_keys("Abulas iela 2 LV1026 Riga")
addres_2=driver.find_element(By.ID, "NewAddressSelection_Address_Line2")
addres_2.clear()
addres_2.send_keys("Abulas iela 2 LV1026 Riga")
city=driver.find_element(By.ID, "NewAddressSelection_Address_Town")
city.clear()
city.send_keys("Riga")
country=driver.find_element(By.ID, "NewAddressSelection_Address_RegionName")
country.clear()
country.send_keys("Latvia")
postcode=driver.find_element(By.ID, "NewAddressSelection_Address_Postcode")
postcode.clear()
postcode.send_keys("1000")
phone=driver.find_element(By.ID, "TelephoneNumber")
phone.clear()
phone.send_keys("+3710000000")
driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div/div/div[2]/div[4]/div[2]/input').click()
total_sum=driver.find_element(By.ID, "TotalValue")
print("The final price of both products is " + total_sum.text)
driver.find_element(By.XPATH, "//*[@id='main-content']/div/div/div/div[2]/div[4]/div[1]/input").click()

driver.quit()