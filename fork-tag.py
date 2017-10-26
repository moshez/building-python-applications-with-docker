#!/usr/bin/env python
import datetime
import subprocess
def cmd(*args):
    subprocess.check_call(list(args))

TAG = (datetime.datetime.now()
               .isoformat().replace(':', '-')
                           .replace('.', '-'))
NAME = 'moshez/pypy3:' + TAG
cmd('docker', 'pull', 'pypy:3-slim')
cmd('docker', 'tag', 'pypy:3-slim', NAME)
cmd('docker', 'push', NAME)
