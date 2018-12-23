register = {k: 0 for k in range(6)}


def addr(a, b, c):
    register[c] = register[a] + register[b]


def addi(a, b, c):
    register[c] = register[a] + b


def mulr(a, b, c):
    register[c] = register[a] * register[b]


def muli(a, b, c):
    register[c] = register[a] * b


def banr(a, b, c):
    register[c] = register[a] & register[b]


def bani(a, b, c):
    register[c] = register[a] & b


def borr(a, b, c):
    register[c] = register[a] | register[b]


def bori(a, b, c):
    register[c] = register[a] | b


def setr(a, _, c):
    register[c] = register[a]


def seti(a, _, c):
    register[c] = a


def gtir(a, b, c):
    register[c] = 1 if a > register[b] else 0


def gtri(a, b, c):
    register[c] = 1 if register[a] > b else 0


def gtrr(a, b, c):
    register[c] = 1 if register[a] > register[b] else 0


def eqir(a, b, c):
    register[c] = 1 if a == register[b] else 0


def eqri(a, b, c):
    register[c] = 1 if register[a] == b else 0


def eqrr(a, b, c):
    register[c] = 1 if register[a] == register[b] else 0


opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
ip = 3
lines = open('data.in').readlines()
while register[ip] < len(lines):
    n, aa, bb, cc = [u for u in lines[register[ip]].strip().split(' ')]
    for op in opcodes:
        if n in str(op):
            op(int(aa), int(bb), int(cc))
    register[ip] += 1
    print(register)
