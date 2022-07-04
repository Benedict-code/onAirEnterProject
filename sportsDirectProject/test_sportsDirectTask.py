from selenium import webdriver
import allure
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest

        #initialization
@allure.severity(allure.severity_level.NORMAL)
class TestonAir:

    @allure.severity(allure.severity_level.MINOR)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://lv.sportsdirect.com/")
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()

    def teardown(self):
        self.driver.quit()

        #Item1 search (lonsdale jersey polo shirt mens)
    @allure.severity(allure.severity_level.NORMAL)
    def test_ItemsSearch(self):
        # def test_Item1Search(self):
        self.driver.find_element(By.ID, "txtSearch").send_keys("polos")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Search']").click()
        self.driver.find_element(By.XPATH, "//li[1]//div[1]//div[1]//div[1]//a[1]//div[1]//img[1]").click()
        self.driver.find_element(By.XPATH, "//img[@alt='White/Navy']").click()

        #item1 view options
        click_next_1 = self.driver.find_element(By.XPATH, "//a[@rel='next']//span")
        for i in range(0, 4):
            click_next_1.click()
            time.sleep(2)

        #item1 size and quantity selection
        self.driver.find_element(By.XPATH, "//div[@id='productVariantAndPrice']//li[1]//a[1]").click()
        self.driver.find_element(By.XPATH, "//span[@class='prodadd']").click()
        self.driver.find_element(By.ID, "aAddToBag").click()
        time.sleep(4)

        #item2 search (Nike Air Zoom Pegasus)
        self.driver.find_element(By.ID, "txtSearch").send_keys("shoes")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Search']").click()
        self.driver.find_element(By.XPATH, '//*[@id="navlist"]/li[1]/div/div/div[1]/a[1]/div/img').click()
        self.driver.find_element(By.XPATH, "//img[@alt='Black/Crimson']").click()

        #item2 view options
        click_next_2 = self.driver.find_element(By.XPATH, "//a[@rel='next']//span")
        for i in range(0, 4):
            click_next_2.click()
            time.sleep(2)

        #item2 size selection and add to bag
        self.driver.find_element(By.XPATH, "//span[normalize-space()='11.5 (47)']").click()
        self.driver.find_element(By.XPATH, "//span[@class='prodadd']").click()
        self.driver.find_element(By.ID, "aAddToBag").click()
        time.sleep(2)

        #items checkout
        bags = self.driver.find_element(By.ID, "bagQuantityContainer")
        action = ActionChains(self.driver)
        action.move_to_element(bags).perform()
        self.driver.find_element(By.XPATH, "//a[@id='aCheckout']//span[contains(text(),'Checkout')]").click()

        #customer account login
        self.driver.find_element(By.ID, "Login_EmailAddress").send_keys("testing001@gmail.com")
        self.driver.find_element(By.ID, "Login_Password").send_keys("Testing070")
        self.driver.find_element(By.ID, "LoginButton").click()

        #Delivery options
        first_name = self.driver.find_element(By.ID, "NewAddressSelection_Address_FirstName")
        first_name.clear()
        first_name.send_keys("test")
        last_name = self.driver.find_element(By.ID, "NewAddressSelection_Address_Surname")
        last_name.clear()
        last_name.send_keys("testing")
        adres_1 = self.driver.find_element(By.ID, "NewAddressSelection_Address_Line1")
        adres_1.clear()
        adres_1.send_keys("Abulas iela 2 LV1026 Riga")
        addres_2 = self.driver.find_element(By.ID, "NewAddressSelection_Address_Line2")
        addres_2.clear()
        addres_2.send_keys("Abulas iela 2 LV1026 Riga")
        city = self.driver.find_element(By.ID, "NewAddressSelection_Address_Town")
        city.clear()
        city.send_keys("Riga")
        country = self.driver.find_element(By.ID, "NewAddressSelection_Address_RegionName")
        country.clear()
        country.send_keys("Latvia")
        postcode = self.driver.find_element(By.ID, "NewAddressSelection_Address_Postcode")
        postcode.clear()
        postcode.send_keys("1000")
        phone = self.driver.find_element(By.ID, "TelephoneNumber")
        phone.clear()
        phone.send_keys("+3710000000")
        self.driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div/div/div[2]/div[4]/div[2]/input').click()
        total_sum = self.driver.find_element(By.ID, "TotalValue")
        print("The final price of both products is " + total_sum.text)
        self.driver.find_element(By.XPATH, "//*[@id='main-content']/div/div/div/div[2]/div[4]/div[1]/input").click()