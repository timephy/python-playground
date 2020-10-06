# https://pymotw.com/2/subprocess/

import sys

sys.stderr.write('stderr: repeater.py: starting\n')
sys.stderr.flush()

sys.stdout.write('YYY\n')
sys.stdout.flush()

# sys.stdout.write('YYY')
# sys.stdout.flush()
print('XXX', flush=True)

while True:
    next_line = sys.stdin.readline()
    # print(f'{next_line=}')

    if not next_line:
        print('if not next_line:')
        break

    sys.stdout.write(f'stdout: {next_line}')  # ends with \n
    sys.stdout.flush()

sys.stderr.write('stderr: repeater.py: exiting\n')
sys.stderr.flush()
