from selenium import webdriver
from time import sleep
from random import uniform as r 
from selenium.webdriver.common.keys import Keys
import urllib.parse

class InstagramProfile:
    def __init__(self, username, password):

        self.driver = webdriver.Chrome()
        self.driver.get('https://instagram.com')
        sleep(r(1,2))
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(r(4,5))
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        sleep(r(3,4))
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        sleep(r(1,2))
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(r(1,2))
        k = False
        while not k:
            try:
                self.driver.find_element_by_xpath("//button[contains(text(),\"Not Now\")]").click()
                sleep(r(1,2))
                k = True
            except:
                k = False
        
    def get_unfollowers(self):

        open('log.txt', 'w').close()
        self.driver.find_element_by_xpath(f"//a[contains(@href, \"{username}\")]").click()
        sleep(r(1,2))
        self.driver.find_element_by_xpath("//a[contains(@href, \"following\")]").click()
        sleep(r(1,2))
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1 
        while last_ht != ht:
            last_ht = ht
            sleep(r(1,2))
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        ing = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
        sleep(r(1,2))
        self.driver.find_element_by_xpath("//a[contains(@href, \"followers\")]").click()
        sleep(r(1,2))
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1 
        while last_ht != ht:
            last_ht = ht
            sleep(r(1,2))
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        ers = [name.text for name in links if name.text != '']

        self.unf = [name for name in ing if name not in ers]

        outfile = open('log.txt', 'w'); 
        outfile.write("\n".join(self.unf)); 
        outfile.close(); 
    
    def clean_log(self):
        open('log.txt', 'w').close()

    def unfollow(self, names):

        for name in range(len(names)):
            if name%20 == 0 and name != 0:
                sleep(1200)
            url = urllib.parse.urljoin('https://instagram.com', names[name])
            self.driver.get(url)
            sleep(r(2,3))
            k = False
            while not k:
                print(name)
                sleep(r(1,2))
                try:
                    sleep(r(1,2))
                    self.driver.find_element_by_xpath("//button[contains(text(),\"Unfollow\")]").click()
                    k = True
                except:
                    k = True
                
username = 'brunoh3n_'
password = 'Maritaca157'

bot = InstagramProfile(username, password)
bot.get_unfollowers()
log = open('log.txt', 'r')
names = [name for name in log]
bot.unfollow(names)