# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 09:52:14 2014

@author: Olivier.Crauste@neel.cnrs.fr
"""

from .jauge import Jauge
import telnetlib

class IPS(telnetlib.Telnet):
    HOST = "192.168.137.222"
    HOST = "127.0.0.1"
    PORT = 7020
    
    def __init__(self, host=HOST, port=PORT):
        super().__init__(host, port)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def ask(self, question):
        if not question.endswith("\n"):
            question += "\n"
        self.write(question.encode('ascii'))
        res = self.read_until(b'\n').decode('ascii').strip()
        return res

class IPS_HE(Jauge):
    name = "IPS_He"
    description = "He level from Oxford Mercury iPS-S"
    def __init__(self, config):
        self.host = config['host']
        self.port = config['port']
    
    def measure(self):
        with IPS(self.host, self.port) as ips:
            he = ips.ask('READ:DEV:DB5.L1:LVL:SIG:HEL:LEV')
            return float(he.split(':')[-1][:-1])

class IPS_N2(Jauge):
    name = "IPS_N2"
    description = "N2 level from Oxford Mercury iPS-S"
    def __init__(self, config):
        self.host = config['host']
        self.port = config['port']
    
    def measure(self):
        with IPS(self.host, self.port) as ips:
            n2 = ips.ask('READ:DEV:DB5.L1:LVL:SIG:NIT:LEV')
            return float(n2.split(':')[-1][:-1])