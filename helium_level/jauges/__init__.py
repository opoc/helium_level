#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import importlib
from . import jauge

def scan_jauge():
    def validate(obj):
        try:
            if not issubclass(obj, jauge.Jauge):
                return False
            return hasattr(obj, 'name') and hasattr(obj, 'description')
        except TypeError:
            return False

    jauges = []
    for module_path in os.listdir(os.path.dirname(__file__)):
        if not module_path.endswith('.py') or module_path=='__init__.py':
            continue
        try:
            module_name = os.path.basename(module_path)[:-3]
            module = importlib.import_module('jauges.' + module_name)
            for jauge_name in dir(module):
                if jauge_name.startswith('__'):
                    continue
                obj = getattr(module, jauge_name)
                if validate(obj):
                    print("Valid module =", jauge_name)
                    jauges.append((module_name, jauge_name,
                        obj.name, obj.description))
        except ImportError:
            print("ImportError on", module_path)
        except SyntaxError:
            print("SyntaxError on", module_path)
    print(jauges)
    return jauges
