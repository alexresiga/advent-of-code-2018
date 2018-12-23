s, e = [3, 7], {'one': [3, 0], 'two': [7, 1]}
while len(s) < 3e7:
    for x in [int(x) for x in str(sum(x[1][0] for x in e.items()))]:
        s.append(x)
    e['one'] = [s[(e['one'][1] + 1 + e['one'][0]) % len(s)], (e['one'][1] + 1 + e['one'][0]) % len(s)]
    e['two'] = [s[(e['two'][1] + 1 + e['two'][0]) % len(s)], (e['two'][1] + 1 + e['two'][0]) % len(s)]
for i in range(len(s)):
    [print(i) for _ in [0] if s[i:i + 6] == [5, 0, 3, 7, 6, 1]]
