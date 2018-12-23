def serialize(aa):
    return aa.strip().replace('#', "").replace("@ ", "").replace(":", "").replace("x", " ").replace(",", " ")


class Claim:
    def __init__(self, id, left, top, w, h):
        self.id = id
        self.left = left
        self.top = top
        self.w = w
        self.h = h


if __name__ == '__main__':
    overlapped = 0
    claims = []
    fabric = [[0 for c in range(1000)] for r in range(1000)]
    with open("data.in", "r") as f:
        for line in f.readlines():
            values = serialize(line).split(' ')
            a, b, c, d, e = map(int, values)
            claim = Claim(a, b, c, d, e)
            claims.append(claim)
            for i in range(claim.top, claim.top + claim.h):
                for j in range(claim.left, claim.left + claim.w):
                    fabric[i][j] += 1
    for claim in claims:
        found = claim.id
        for i in range(claim.top, claim.top + claim.h):
            for j in range(claim.left, claim.left + claim.w):
                if fabric[i][j] != 1:
                    found = False
        if found:
            print(found)
