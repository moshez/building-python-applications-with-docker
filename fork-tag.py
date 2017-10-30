#!/usr/bin/env python
import datetime
import subprocess
def cmd(*args):
    subprocess.check_call(list(args))

IMAGE = 'pypy:3-slim'
TAG = (datetime.datetime.now()
               .isoformat().replace(':', '-')
                           .replace('.', '-'))
NAME = 'moshez/pypy3:' + TAG
cmd('docker', 'pull', IMAGE)
cmd('docker', 'tag', IMAGE, NAME)
cmd('docker', 'push', NAME)
