#This module is dedicated to post and get from an Restful API
#using the requests package

import requests

def login(username,password):
    """Login some user"""
    url = 'http://api.example.br/login'
    params = {'username': username, 'password': password}
    r = requests.post(url,params=params)
    