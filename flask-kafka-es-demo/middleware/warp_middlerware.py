import logging
import os
from flask import request, g, jsonify
import time


def register_wrap_middleware(app):
    @app.before_request
    def wrap_before():
        print("wrap_before_request")

    @app.after_request
    def wrap_after(response):
        print("wrap_after_request")
        return response
