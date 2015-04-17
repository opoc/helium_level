#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib

MSG_STUB="""From: {}
To: {}
Subject: Helium level alert

The Helium level is too low ({})."""


def send_email(email_config, value=''):
    fromaddr = email_config['dest'].split()[0]
    toaddrs = ', '.join(email_config['dest'].split())
    with smtplib.SMTP(email_config['server']) as smtp:
        smtp.set_debug_level(1)
        smtp.sendmail(fromaddr, toaddrs,
            MSG_STUB.format(fromaddr, toaddrs, value).replace('\n', '\r\n'))
