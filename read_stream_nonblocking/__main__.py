import sys
import time

from nbsr import NonBlockingStreamReader


nbsr = NonBlockingStreamReader(sys.stdin)


while True:
    # output = nbsr.readline()  # no timeout arg will not block
    # if output:
    #     print(f'if output: {output=}')
    # else:
    #     print(f'if not output: {output=}')

    # Python 3.8 style variant with 'walrus operator'.
    # Reads all lines after another, does not wait for another 'while True'
    while output := nbsr.readline():
        print(f'while output: {output=}')

    print('sleeping 1s')
    time.sleep(1)  # sleep for usability in cli
