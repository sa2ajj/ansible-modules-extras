#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Perforce support for Ansible
"""

DOCUMENTATION = """
module: perforce
author:
- 'Mikhail Sobolev'
version_added: '???'
short_description: Deploy software or files from Perforce
description:
- why do we use list here?
options:
  port:
    reqiured: true
    description:
    - description of the port
  client:
    reqiured: true
    description:
    - some description of the 'client'
  dest:
    reqiured: true
    description:
    - some description of the 'dest'
  charset:
    reqiured: false
    description:
    - some description of the 'charset'
  tickets:
    reqiured: false
    description:
    - some description of the 'tickets'
  trust:
    reqiured: false
    description:
    - some description of the 'trust'

    P4CLIENTPATH     Directories client can access   Perforce Command Reference
    P4IGNORE         Name of ignore file             Perforce Command Reference
    P4PASSWD         User password passed to server  p4 help passwd
    P4SSLDIR         SSL server credential directory Perforce Command Reference
    P4USER           Perforce user name              p4 help usage

"""
