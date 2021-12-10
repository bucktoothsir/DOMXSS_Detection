#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ©  2021-12-09 12:43 bucktoothsir <rsliu.xd@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from flask import Flask, make_response, send_from_directory

app = Flask(__name__)

@app.route("/<filename>")
def get_file(filename):
    response = make_response(
            send_from_directory('data', filename)
            )
    return response


if __name__ == "__main__":
    app.run()

