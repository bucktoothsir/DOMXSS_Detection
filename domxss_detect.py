#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ©  2021-12-06 15:19 bucktoothsir <rsliu.xd@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import os
import argparse
from webdriver.utils import add_drivers_to_path
from domxss import DomXSSDetector


def main(url, browser, rule, attack_vectors, scan_result_filename):
    domxss_detector = DomXSSDetector(browser)
    if rule == 'payload':
        print('Scan by payload starts.')
        scan_result, scan_info =  domxss_detector.scan_by_payload(url, attack_vectors)
        print('Scan by payload finishes')
        if scan_result:
            print('%s is vunlerable.' % url)
            if scan_info:
                print(scan_info)
        else:
            print('%s is not vunlerable.' % url)
    if rule == 'reg':
        print('Scan by regular expression starts.')
        domxss_detector.scan_by_reg(url, scan_result_filename)
        print('Scan by regular expression finishes.')
        print('Scan results is stored in %s.' % scan_result_filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str, help='Input the url for detection')
    parser.add_argument('--browser', type=str, nargs='?', default='firefox', help='Browser')
    parser.add_argument('--rule', type=str, nargs='?', default='payload', help='scan by payload or regular expression')
    parser.add_argument('--payload', type=str, nargs='?', default='', help='Payload to attack the url')
    parser.add_argument('--payload_file', type=str, nargs='?', default='', help='Payload file to attack the url')
    parser.add_argument('--scan_result_filename', type=str, nargs='?', default='domxss_detail.txt', help='file to store the scan result, only works for scan by regular expression')
    args = parser.parse_args()
    attack_vectors = []
    if args.payload:
        attack_vectors.append(args.payload)
    elif args.payload_file:
        with open(args.payload_file) as f:
            for line in f:
                line = line.strip('\n')
                attack_vectors.append(line)
    with add_drivers_to_path(os.path.dirname(__file__)):
        main(args.url, args.browser, args.rule, attack_vectors, args.scan_result_filename)
