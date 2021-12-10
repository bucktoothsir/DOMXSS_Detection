#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ©  2021-12-09 12:43 bucktoothsir <rsliu.xd@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from flask import Flask, make_response, send_from_directory
from test_config import *

app = Flask(__name__)

@app.route("/data/<filename>")
def get_file(filename):
    response = make_response(
            send_from_directory('data', filename)
            )
    return response


if __name__ == "__main__":
    app.run(port=PORT)

