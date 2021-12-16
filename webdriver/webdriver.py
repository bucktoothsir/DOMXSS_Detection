#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ©  2021-12-01 21:21 bucktoothsir <rsliu.xd@gmail.com>
#
# Distributed under terms of the MIT license.

from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.common import exceptions
from selenium.webdriver.common.by import By


class WebDriver():
    """Class WebDriver is a wrapper of selenium.webdriver.
    Check more details at https://www.selenium.dev/documentation/webdriver/
    """

    def __init__(self, browser='firefox'):
        self.browser = browser.lower()
        if self.browser == 'firefox':
            options = firefox_options()
            options.add_argument('--headless')
            self.driver = webdriver.Firefox(options=options)
        elif self.browser == 'chrome':
            options = chrome_options()
            options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=options)
        else:
            raise NameError(
                    '%s is not a valid browser name'
                    'please choose one from chrome and firefox',
                    self.browser)

    def get(self, url, retry=3):
        """
        Loads a web page in the current browser session.
        """
        try:
            self.driver.get(url)
        except exceptions.InvalidSessionIdException:
            # pause and retry
            try:
                sleep(100)
            except KeyboardInterrupt:
                pass
            if (retry >= 0):
                self.get(url, retry-1)
        except exceptions.TimeoutException:
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
        except exceptions.InvalidSessionIdException:
            # pause and retry
            try:
                sleep(100)
            except KeyboardInterrupt:
                pass
            if (retry >= 0):
                return self.find_tag(value, retry-1)
        except exceptions.TimeoutException:
            if retry > 0:
                return self.find_tag(value, retry-1)

    def get_alert_text(self):
        try:
            alert_dialog = self.driver.switch_to.alert
            alert_text = alert_dialog.text
            alert_dialog.accept()
            return alert_text
        except exceptions.NoAlertPresentException:
            return ''
