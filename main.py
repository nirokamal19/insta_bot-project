from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# USER INPUT
user_name = input("Please enter Instagram Username...")
pw = input("Please enter Instagram Password...")
hash1 = input("Please enter first # to like...")
hash2 = input("Please enter second # to like...")
hash3 = input("Please enter third # to like...")


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)

        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(5)


    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)


        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if "/p/" in href]
        print(hashtag + ' photos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                elem = driver.find_elements_by_xpath("//div[contains(@class, '_9AhH0')]")[0]

                actions = ActionChains(driver)
                actions.double_click(elem)
                actions.perform()
                time.sleep(20)
                
            except Exception as e:
                time.sleep(2)

test = Login(user_name, pw)
test.login()
hashtags = [hash1, hash2, hash3]
[test.like_photo(tag) for tag in hashtags]