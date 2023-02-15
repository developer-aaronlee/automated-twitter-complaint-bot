from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

PROMISED_DOWN = 300
PROMISED_UP = 300
TWITTER_EMAIL = "pythonautomationapp@gmail.com"
TWITTER_PASSWORD = "lsr211425"
TWITTER_USERNAME = "Aaron10627913"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_driver = Service("/Applications/chromedriver")
        self.driver = webdriver.Chrome(service=self.chrome_driver)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.CSS_SELECTOR, ".start-button a").click()
        time.sleep(45)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(3)
        login_email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        login_email.send_keys(TWITTER_EMAIL)
        login_email.send_keys(Keys.ENTER)
        time.sleep(3)
        login_username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        login_username.send_keys(TWITTER_USERNAME)
        login_username.send_keys(Keys.ENTER)
        time.sleep(3)
        show_password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[2]/div/div')
        show_password.click()
        time.sleep(3)
        login_password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        login_password.send_keys(TWITTER_PASSWORD)
        login_password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_box = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        tweet_box.click()
        tweet_message = f"Hey Verizon, why is my internet speed {self.down}down/{self.up}up " \
                       f"when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_box.send_keys(tweet_message)
        time.sleep(3)
        twit_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        twit_button.click()
        time.sleep(10)


bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
print(f"download: {bot.down}\nupload: {bot.up}")

bot.tweet_at_provider()



bot.driver.quit()
