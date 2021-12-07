#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ©  2021-12-01 22:16 bucktoothsir <rsliu.xd@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from selenium.common.exceptions import UnexpectedAlertPresentException
from webdriver import WebDriver
from .domxss_alert_info import DomAlertInfo
from .domxss_detector_config import UNLIKELY_STR, ATTACK_VECTORS

class DomXSSDetector():
    def __init__(self, browser='firefox'):
        self.webdriver = WebDriver(browser)
        self.vulnerable = False
        self._unlikely_str = UNLIKELY_STR
        self._attack_vecotrs = ATTACK_VECTORS
        
    def _alert_helper(url, attack_vector, tag_name='', attribute_id='', attribute_name=''):
        alert_text = self.webdriver.get_alert_text()
        if alert_text == self.UNLIKELY_STR:
            dom_alert_info = DomAlertInfo(url, attack_vector, tag_name=tag_name, attribute_id=attribute_id, attribute_name=attribute_name)
            return dom_alert_info
        else:
            return None

    def _scan_helper(self, url, attack_vector):
        try:
            self.webdriver.get(url)
        except UnexpectedAlertPresentException as e:
            dom_alert_info = self._alert_helper(url, attack_vector)
            if dom_alert_info:
                return dom_alert_info
            
        possible_domxss_triggers = list()
        try:
            input_elements = self.webdriver.find_tag('input')
            if input_elements:
                possible_domxss_triggers.extend(input_elements)
            buttion_elements = self.webdriver.find_tag('button')
            if buttion_elements:
                possible_domxss_triggers.extend(buttion_elements)
        except UnexpectedAlertPresentException as e:
            dom_alert_info = self._alert_helper(url, attack_vector)
            self.vulnerable = True
            if dom_alert_info:
                return dom_alert_info
        
        for i in range(len(possible_domxss_triggers)):
            possible_domxss_trigger = possible_domxss_triggers[i]
            tag_name = possible_domxss_trigger.tag_name
            attribute_id = possible_domxss_trigger.get_attribute('id')
            attribute_name = possible_domxss_trigger.get_attribute('name')
            try:
                if tag_name == 'input':
                    possible_domxss_trigger.send_keys(attack_vector)
                element.click();
            except UnexpectedAlertPresentException as e:
                dom_alert_info = self._alert_helper(url, attack_vector, tag_name=tag_name, attribute_id=attribute_id, attribute_name=attribute_name)
                if dom_alert_info:
                    return dom_alert_info

            try: 
                self.webdriver.get(url)
            except UnexpectedAlertPresentException as e:
                dom_alert_info = self._alert_helper(url, attack_vector, tag_name=tag_name, attribute_id=attribute_id, attribute_name=attribute_name)
                if dom_alert_info:
                    return dom_alert_info

            possible_domxss_triggers = []
            try: 
                input_elements = self.webdriver.find_tag('input')
                if input_elements:
                    possible_domxss_triggers.extend(input_elements)
                buttion_elements = self.webdriver.find_tag('button')
                if buttion_elements:
                    possible_domxss_triggers.extend(button_elements)
            except UnexpectedAlertPresentException as e:
                dom_alert_info = self._alert_helper(url, attack_vector, tag_name=tag_name, attribute_id=attribute_id, attribute_name=attribute_name)
                if dom_alert_info:
                    return dom_alert_info

        try:
            all_elements = self.webdriver.find_tag('div')
        except UnexpectedAlertPresentException as e:
            dom_alert_info = self._alert_helper(url, attack_vector, tag_name=tag_name, attribute_id=attribute_id, attribute_name=attribute_name)
            if dom_alert_info:
                return dom_alert_info

        for i in range(len(all_elements)):
            element = all_elements[i]
            tag_name = element.tag_name
            attribute_id = element.get_attribute('id')
            attribute_name = element.get_attribute('name')
            try:
                element.click();
            except UnexpectedAlertPresentException as e:
                dom_alert_info = self._alert_helper(url, attack_vector, tag_name=tag_name, attribute_id=attribute_id, attribute_name=attribute_name)
                if dom_alert_info:
                    return dom_alert_info
            try: 
                self.webdriver.get(url)
            except UnexpectedAlertPresentException as e:
                dom_alert_info = self._alert_helper(url, attack_vector, tag_name=tag_name, attribute_id=attribute_id, attribute_name=attribute_name)
                if dom_alert_info:
                    return dom_alert_info

            try:
                all_elements = self.webdriver.find_tag('div')
            except UnexpectedAlertPresentException as e:
                dom_alert_info = self._alert_helper(url, attack_vector, tag_name=tag_name, attribute_id=attribute_id, attribute_name=attribute_name)
                if dom_alert_info:
                    return dom_alert_info

        return None 

    def scan(self, url, attack_vecotrs=list()):
        if not attack_vecotrs:
            attack_vecotrs = self._attack_vecotrs
        for attack_vector in attack_vecotrs:
            url += attack_vector
            result = self._scan_helper(url, attack_vector);
            if result:
                tag_name = result.get_tag_name()
                other_info = ''
                if tag_name:
                    other_info = 'Tag name: %s, Att name: %s, Att id: %s' % (tag_name, result.get_attribute_name, result.get_attribute_id)
                self.vulnerable = true;
                return true;
        return false;
