#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ©  2021-12-01 22:51 bucktoothsir <rsliu.xd@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
class DomAlertInfo():
    def __init__(url, attack, tag_name='', attribute_id='', attribute_name=''):
        self.url = url
        self.attack = attack
        self.tag_name = tag_name
        self.attribute_id = attribute_id
        self.attribute_name = attribute_name
        self.serial_version_uid = 1

    def get_url():
        return self.url
    
    def get_attack():
        return self.attack
    
    def get_serial_version_uid():
        return self.serial_version_uid
    
    def get_tag_name():
        return self.tag_name
    
    def get_attribute_name():
        return self.attribute_name
    
    def get_attribute_id():
        return self.attribute_id
