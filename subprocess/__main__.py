import subprocess


def pprint(tuple):
    print("=> stdout:", None if tuple[0] == '' else '⬇')
    print(tuple[0])
    print("=> stderr:", None if tuple[1] == '' else '⬇')
    print(tuple[1])


p = subprocess.Popen("python repeater.py", shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE, stdin=subprocess.PIPE,
                     universal_newlines=True)

print(p)
print(p.stdout, p.stdin, p.stderr)

print()

print('p.stderr.readline()', p.stderr.readline())

print('p.stdout.readline()', p.stdout.readline())
print('p.stdout.readline()', p.stdout.readline())

for i in range(10):
    print(i, 'will write')
    p.stdin.write(f'{i}\n')
    p.stdin.flush()
    print(i, 'after write')
    print(i, 'p.stdout.readline()', p.stdout.readline())

# print('will p.stderr.readline()')
# print(p.stderr.readline())

# pprint(p.communicate('sleep 5 ; ls -lah'))
