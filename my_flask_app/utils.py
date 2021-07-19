# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import time

from flask import flash


def flash_errors(form, category="warning"):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{getattr(form, field).label.text} - {error}", category)


class ExternalService:
    def get_user_info(self, uid):
        time.sleep(2)
        return {}


def check_captcha(s):
    raise Exception("err")
