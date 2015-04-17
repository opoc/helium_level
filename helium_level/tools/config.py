#!/usr/bin/python3

"""Read and write config files."""

from configparser import ConfigParser
import os

DEFAULT = {
    'LEVEL': {
        'top': '100',
        'high': '80',
        'warn': '25',
        'low': '10',
        'bottom': '0'},
    'RATE': {
        'slow': 30,
        'fast': 0.5},
    'JAUGES': {
        'active': ''},
    'EMAIL': {
        'Alert': "False",
        'server': 'smtp.grenoble.cnrs.fr',
        'username': '',
        'password': '',
        'dest': 'email@test.com\nemail2@test.com'},
    }


def load(configpath):
    config = ConfigParser()
    try:
        if os.path.exists(configpath):
            config.read(configpath)
        else:
            config.read_dict(DEFAULT)
    except AttributeError:
        config.read_dict(DEFAULT)
    return config


def save(config, configpath):
    config.write(open(configpath, 'w'))
