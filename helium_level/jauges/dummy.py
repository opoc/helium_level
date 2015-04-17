#!/usr/bin/python
# -*- coding: utf-8 -*-

from .jauge import Jauge
import random


class Dummy(Jauge):
    name = "dummy"
    description = "Dummy jauge for test purpose."

    def __init__(self, config):
        self.config = config
        self.min_value = self.config.getfloat('min_value')
        self.max_value = self.config.getfloat('max_value')

    def measure(self):
        return random.uniform(self.min_value, self.max_value)
