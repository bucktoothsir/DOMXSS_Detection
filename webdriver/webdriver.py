#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ©  2021-12-01 21:21 bucktoothsir <rsliu.xd@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
#from .utils import add_drivers_to_path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

class WebDriver():
    def __init__(self, browser='firefox'):
        self.browser = browser.lower()
        if self.browser == 'firefox':
            options = Options()
            options.add_argument('--headless')
            self.driver = webdriver.Firefox(options=options)
        
        #other browsers to do
        
        else:
            raise NameError('%s is not a valid browser name, please input one from blabla', self.browser)
            
    def get(self, url, retry=3):
        """
        Loads a web page in the current browser session.
        """
        try:
            self.driver.get(url)
        except InvalidSessionIdException as err:
            # pause and retry
            try:
                sleep(100)
            except KeyboardInterrupt as e:
                pass
            if (retry >= 0):
                self.get(url, retry-1)
        except TimeoutException as err:
            if retry > 0:
                self.get(url, retry-1)
    
    def get_html(self, url, retry=3):
        """
        Get HTML of the URL
        """
        self.get(url, retry=retry)
        html = self.driver.page_source
        return html


    def find_tag(self, value, retry=3):
        """
        Find elements by value of tag name
        """ 
        try:
            return self.driver.find_elements(By.TAG_NAME, value)
        except InvalidSessionIdException as err:
            # pause and retry
            try:
                sleep(100)
            except KeyboardInterrupt as e:
                pass
            if (retry >= 0):
                return self.find_tag(value, retry-1)
        except TimeoutException as err:
            if retry > 0:
                return self.find_tag(value, retry-1)
                
    def get_alert_text(self):
        try:
            alert_dialog = driver.switch_to.alert
            alert_text = alertDialog.text;
            alert_dialog.accept();
            return alert_text
        except NoAlertPresentException:
            return ''
