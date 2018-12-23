from collections import defaultdict

register = {k: 0 for k in range(4)}
freq = defaultdict(list)


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


opcodes = [(addr, 14), (addi, 0), (mulr, 15), (muli, 8), (banr, 10), (bani, 1), (borr, 3), (bori, 5), (setr, 7),
           (seti, 9), (gtir, 2), (gtri, 11), (gtrr, 6), (eqir, 12), (eqri, 13), (eqrr, 4)]
operations = {eqrr: 4}
content = [x.strip() for x in open('data.in').readlines()]
content = [x for x in content if x != '']
groups = zip(*(iter(content),) * 3)

# for x in groups:
#     before = x[0][x[0].find('[') + 1:-1].split(', ')
#     op = x[1].split(' ')
#     after = x[2][x[0].rfind('['):]
#     cnt = 0
#     for opcode in opcodes:
#         register[0], register[1], register[2], register[3] = [int(x) for x in before]
#         n, aa, bb, cc = [int(x) for x in op]
#         opcode(aa, bb, cc)
#         if str(list(register.values())) == after:
#             freq[n].append(opcode)
#             cnt += 1
#
# for x in freq.items():
#     if x[0] not in [4, 11, 12, 13, 6, 2, 10, 1, 9, 7, 3, 5, 0, 15]:
#         print(x[0], end=' ')
#         print(Counter(x[1]).most_common())

register[0], register[1], register[2], register[3] = [0] * 4
for x in open('data.in').readlines():
    n, aa, bb, cc = [int(u) for u in x.split(' ')]
    for d in opcodes:
        if n == d[1]:
            d[0](aa, bb, cc)
print(register)
