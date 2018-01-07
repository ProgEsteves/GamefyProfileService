# -*- coding: utf-8 -*-
"""module"""

from eve import Eve

APP = Eve()

@APP.route('/api/v0/user/<user>', methods=['GET', 'POST'])
def get_user_profile(user):
    """get user profile"""
    from profile import Profile
    return Profile(user).get_user()

@APP.route('/api/v0/welcome/<user>', methods=['GET', 'POST'])
def print_welcome(user):
    """print welcome user name"""
    from profile import Profile
    return "Welcome " + Profile(user).get_user()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080)
