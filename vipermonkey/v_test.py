#!/usr/bin/env python

import sys
from vmonkey import *

colorlog.basicConfig(level=logging.INFO)

f=open(sys.argv[1],'r')
x=f.read()
f.close()

r=process_file('','',x, strip_useless=True)

print r[0][1]
