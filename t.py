#!/usr/bin/env python3

import sys
from todoist.api import TodoistAPI

if len(sys.argv) < 2:
  print("Usage: todoist <msg>")
  sys.exit()

msg = ' '.join(sys.argv[1:])
msg = msg.strip()
if msg:
    api = TodoistAPI('244edfbafbfddf12067bdbd866805d928ade76c1')
    print(api.quick.add(msg))
