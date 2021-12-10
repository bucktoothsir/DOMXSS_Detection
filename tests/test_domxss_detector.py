# /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ©  2021-12-08 20:14 bucktoothsir <rsliu.xd@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from unittest import mock

from domxss import DomXSSDetector
from domxss import DomAlertInfo
from .test_config import *


import pytest


@pytest.fixture
def get_domxss_detector():
    return DomXSSDetector()

@pytest.mark.parametrize('url',
                      ['LocationHashEval.html',
                       'LocationHashReplace.html',
                       'LocationHashFormAction.html',
                       'LocationHashSetTimeout.html'])
def test_scan_by_payload(url, get_domxss_detector):
    domxss_detector = get_domxss_detector
    url = HTTP_SERVER_ADDRESS + ':' + str(PORT) + '/' + url
    result = domxss_detector.scan_by_payload(url)
    assert result == True



@mock.patch('domxss.domxss_detector.WebDriver', mock.MagicMock(return_value=None))
class TestScanByPayload():

    def test_is_vulnerable(self, monkeypatch):
        detector = DomXSSDetector()
        assert detector.vulnerable is False

        def mock_payload_scan_helper(*args, **kwargs):
            return DomAlertInfo('test url', None)

        monkeypatch.setattr(detector, '_payload_scan_helper', mock_payload_scan_helper)

        assert detector.scan_by_payload('test url') is True
        assert detector.vulnerable is True


    def test_is_not_vulnerable(self, monkeypatch):
        detector = DomXSSDetector()
        assert detector.vulnerable is False

        def mock_payload_scan_helper(*args, **kwargs):
            return None

        monkeypatch.setattr(detector, '_payload_scan_helper', mock_payload_scan_helper)

        assert detector.scan_by_payload('test url') is False
        assert detector.vulnerable is False


    def test_empty_vectors_should_not_be_vulnerable(self, monkeypatch):
        detector = DomXSSDetector()
        monkeypatch.setattr(detector, '_attack_vecotrs', [])
        assert detector.scan_by_payload('test url') is False
        assert detector.vulnerable is False


    def test_scan_by_given_vectors_if_present(self, monkeypatch):
        detector = DomXSSDetector()
        attack_vecotrs = ['a1', 'a2']
        default_vectors = ['v1', 'v2']
        monkeypatch.setattr(detector, '_attack_vecotrs', default_vectors)

        called_vectors = []
        def mock_payload_scan_helper(url, vector):
            called_vectors.append(vector)
            return None

        monkeypatch.setattr(detector, '_payload_scan_helper', mock_payload_scan_helper)
        detector.scan_by_payload('test url', attack_vecotrs)
        assert called_vectors == attack_vecotrs


    def test_empty_vectors_should_use_default_vectors(self, monkeypatch):
        detector = DomXSSDetector()
        default_vectors = ['v1', 'v2']
        monkeypatch.setattr(detector, '_attack_vecotrs', default_vectors)

        called_vectors = []
        def mock_payload_scan_helper(url, vector):
            called_vectors.append(vector)
            return None

        monkeypatch.setattr(detector, '_payload_scan_helper', mock_payload_scan_helper)
        detector.scan_by_payload('test url')
        assert called_vectors == default_vectors
