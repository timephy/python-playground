import subprocess


p = subprocess.Popen("python repeater.py", shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE, stdin=subprocess.PIPE,
                     universal_newlines=True)

print(p)
print(p.stdout, p.stdin, p.stderr)

print()

print('p.stderr.readline()', p.stderr.readline())

print('p.stdout.readline()', p.stdout.readline())
print('p.stdout.readline()', p.stdout.readline())

for i in range(5):
    # p.stdin.write(f'{i}\n')
    # p.stdin.flush()
    print(i, file=p.stdin, flush=True)

    print(i, 'p.stdout.readline()', p.stdout.readline())
