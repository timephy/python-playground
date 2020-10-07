import sys
import time

from nbsr import NonBlockingStreamReader


nbsr = NonBlockingStreamReader(sys.stdin)


while True:
    output = nbsr.readline()  # no timeout arg will not block
    if output:
        print(f'if output: {output=}')
    else:
        print(f'if not output: {output=}')
    time.sleep(1)  # sleep for usability in cli
