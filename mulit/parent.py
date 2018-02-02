import sys
import time
from subprocess import Popen, PIPE

with Popen([sys.executable, 'child.py'],
           stdin=PIPE, # redirect process' stdin
           bufsize=1, # line-buffered
           universal_newlines=True # text mode
           ) as process:
    a = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    for i in a:
        time.sleep(.5)
        print(i, file=process.stdin, flush=True)