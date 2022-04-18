from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
username = input("Enter your username or e-mail: ")
password = input("Enter your password: ")
class twitterBot:
    def __init__(self,username,password):
        self.loop = None
        self.seconds = None
        self.tweet = None
        self.username = username
        self.password = password
    def autoTweet(self,loop,seconds,tweet=[]):
        self.tweet = tweet
        self.seconds = seconds
        self.loop = loop
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=option)
        browser.get("https://twitter.com/i/flow/login")
        time.sleep(1)
        username = browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        username.send_keys(self.username)
        username.send_keys(Keys.ENTER)
        time.sleep(1)
        password = browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        for i in range(0,self.loop):
            sendTweet = browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            sendTweet.send_keys(tweet[i])
            sendTweet.send_keys(Keys.CONTROL + Keys.ENTER)
            time.sleep(self.seconds)       
user = twitterBot(username,password)
def run():
    input1 = input("How many tweets do you want to send?\n")
    while True:
        if input1.isdigit():
            input1 = int(input1)
            break
        else:
            print("Input must be number!")
            input1 = input("How many tweets do you want to send?\n")
    tweetList = list()
    for i in range(0,input1):
            tweetList.append(input("Enter your tweet: "))
    input2 = input("How many seconds do you want to wait between tweets?\n")
    while True:
        if input2.isdigit():
            input2 = int(input2)
            break
        else:
            print("Input must be number!")
            input2 = input("How many seconds do you want to wait between tweets?\n")
    print("Program is running...")
    user.autoTweet(input1,input2,tweetList)
    print("Done!")
run()
