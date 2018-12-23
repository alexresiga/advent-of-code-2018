def f(i):
    ans, n_ch, n_md, md = 0, v[i], v[i + 1], []
    i += 2
    for _ in range(n_ch):
        i, val = f(i)
        md.append(val)
    return i + n_md, sum(v[i:i + n_md]) if n_ch == 0 else sum(md[k - 1] for k in v[i:i + n_md] if 0 < k <= len(md))


v = list(map(int, open('data.in', 'r').read().split(' ')))
print(f(0)[1])
