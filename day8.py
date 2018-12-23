alist = [int(x) for x in open('data.in').read().split(' ')]
child, meta = alist[0], alist[1]
print(alist[-meta:])
metadata = sum(alist[-meta:])
alist = alist[2:-meta]
i = 0
while alist:
    if not alist[i]:
        child = alist[i]
        metadata += sum(a for a in alist[i+2: alist[i+1]+2])
        meta = alist[i+1]
        ceva = alist[2+alist[i+1]:]
        alist[:] = ceva
    else:
        child = alist[i]
        metadata += sum(alist[-(alist[i]):])
        meta = alist[i+1]
        ceva = alist[2:-(i+1)]
        alist[:] = ceva

print(alist)
print(metadata)