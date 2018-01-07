# -*- coding: utf-8 -*-
"""utils"""

from collections import namedtuple
import requests
from flask import json

def _json_object_hook(hook):
    """json_object_hook"""
    return namedtuple('O', hook.keys())(*hook.values())

def json2obj(data):
    """json2obj"""
    return json.loads(data, object_hook=_json_object_hook)

### User class
class User(object):
    """user"""

    def __init__(self):
        self.name = "Test"


### Profile class
class Profile(object):
    """profile"""

    def __init__(self, user):
        self.__user = user

    @property
    def user(self):
        """get user"""
        return self.__user

    @user.setter
    def user(self, value):
        """set user"""
        self.__user = value

    def get_user(self):
        """get user"""
        request = requests.get("https://api.github.com/users/" + self.__user)
        if request.ok:
            obj = json2obj(request.content)
            return obj.name
        else:
            request.raise_for_status()

### Test
if __name__ == '__main__':
    profile = Profile("ProgEsteves")
    print(profile.get_user())
