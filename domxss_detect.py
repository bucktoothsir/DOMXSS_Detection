#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ©  2021-12-06 15:19 bucktoothsir <rsliu.xd@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import argparse
from domxss import DomXSSDetector


def main(url, browser, attack_vectors):
    domxss_detector = DomXSSDetector(browser)
    domxss_detector.scan(url, attack_vectors)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str, help='Input the url for detection')
    parser.add_argument('--payload', type=str, nargs='?', default='', help='Payload to attack the url')
    parser.add_argument('--payload_file', type=str, nargs='?', default='', help='Payload file to attack the url')
    parser.add_argument('--browser', type=str, nargs='?', default='firefox', help='Browser')
    args = parser.parse_args()
    attack_vectors = []
    if args.payload:
        attack_vectors.append(args.payload)
    elif args.payload_file:
        with open(args.payload_file) as f:
            for line in f:
                line = line.strip('\n')
                attack_vectors.append(line)
    main(args.url, args.browser, attack_vectors)
