#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Routines for measuring the helium level with an Agilent source.

Requires pyserial."""

from .jauge import Jauge
import serial

class Agilent(Jauge):
    name = "agilent"
    description = "Agilent jauge"

    def __init__(self, config):
        self.config = config
        self.ser = serial.Serial()

    def measure(self):
        return 32  # random number: choosed with a dice :) 
