# -*- coding:utf8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


class InsBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        sleep(2)
        self.driver.find_element_by_xpath('//input[@name=\"username\"]')\
            .send_keys(username)
        self.driver.find_element_by_xpath('//input[@name=\"password\"]') \
            .send_keys(pw)
        self.driver.find_element_by_xpath('//input[@name=\"password\"]').send_keys(Keys.RETURN)
        sleep(4)
        self.driver.get("https://www.instagram.com/"+ self.username)
        sleep(2)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print('Seguidores: \n')
        print(followers)
        print(len(followers))
        print('Seguidos: \n')
        print(following)
        print(len(following))
        print('No seguidores: \n')
        print(not_following_back)
        print(len(not_following_back))

    def _get_names(self):
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;""", scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        return names

pw = open('pw.txt', 'r')
pw = pw.read()
Bot = InsBot('juandavidpolo1', pw)
Bot.get_unfollowers()
