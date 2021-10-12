from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class FillerGoogleForm:

    def __init__(self, url):
        self.url = url
        google_drive_path = "/home/freadrix/MyFiles/development/chromedriver"
        # options = webdriver.ChromeOptions()
        # options.add_argument("-incognito")
        self.driver = webdriver.Chrome(executable_path=google_drive_path)  # options=options

    def fill_form(self, answer_for_first_question, answer_for_second_question, answer_for_third_question):
        """
        Method fill google form and sen answers
        :param answer_for_first_question:
        :param answer_for_second_question:
        :param answer_for_third_question:
        """
        self.driver.get(self.url)
        time.sleep(1)
        answer_first = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div'
                                                      '/div[2]/div/div[1]/div/div[1]/input')
        answer_first.send_keys(answer_for_first_question)
        answer_second = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div'
                                                            '/div[2]/div/div[1]/div/div[1]/input')
        answer_second.send_keys(answer_for_second_question)
        answer_third = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div'
                                                           '/div[2]/div/div[1]/div/div[1]/input')
        answer_third.send_keys(answer_for_third_question)
        send_button = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
        send_button.click()
        time.sleep(1)

    def open_sheet(self):
        """
        Method just open google sheet, which was filling before  : NOT WORKING
        """
        self.driver.get(self.url)
        time.sleep(10)
