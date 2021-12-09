#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ©  2021-12-08 20:14 bucktoothsir <rsliu.xd@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import pytest
from http.server import HTTPServer
import random
from domxss import DomXSSDetector

class TestDomXSSDector():
    def __init__(self):
        self.domxss_detector = DomXSSDetector()

    @pytest.mark.parametrize('url',
                          ['LocationHashEval.html',
                           'LocationHashReplace.html',
                           'LocationHashFormAction.html',
                           'LocationHashSetTimeout.html'])
    def test_scan_by_payload(url):
        port = random.randint(PORT_START, PORT_END)
        server_address = server_address + ':' + str(port) + '/' + HTML_FOLDER
        with HTTPServer(server_address) as httpd:
            print("HTTP serving at port", port)
            httpd.serve_forever()
            result = self.domxss_detector.scan_by_payload(url)
            assert result == True
