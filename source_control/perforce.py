#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Perforce support for Ansible
"""

DOCUMENTATION = """\
---
module: perforce
author:
- 'Mikhail Sobolev'
version_added: '???'
short_description: Deploy software or files from Perforce
description:
- why do we use list here?
options:
  port:
    reqiured: false
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
  revision:
    reqiured: false
    default: "#head"
    description:
    - some description of the 'revision'
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
  user:
    reqiured: false
    description:
    - some description of the 'user'
  passwd:
    reqiured: false
    description:
    - some description of the 'passwd'
"""

EXAMPLES = """\
"""

def main():
    """
    ...
    """
    module = AnsibleModule(
        argument_spec=dict(
            client=dict(
                reqiured=True
            ),
            dest=dict(
                reqiured=True
            ),
            revision=dict(
                reqiured=False,
                default='#head'
            ),
            charset=dict(
                reqiured=False
            ),
            tickets=dict(
                reqiured=False
            ),
            trust=dict(
                reqiured=False
            ),
            user=dict(
                reqiured=False
            ),
            passwd=dict(
                reqiured=False
            )
        ),
    )

    module.exit_json(changed=True)

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
