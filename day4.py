class Shift:
    def __init__(self, guard, events):
        self.guard = guard
        self.events = events

    def total(self):
        return sum(bb.get_minutes() - aa.get_minutes() for aa, bb in zip(self.events[0::2], self.events[1::2]))


class Event:
    def __init__(self, _date: str, _action: list):
        self.date = _date
        self.action = _action

    def __lt__(self, other):
        return self.date < other.date

    def get_minutes(self):
        return int(self.date[self.date.find(' ')+1:].split(':')[1])


if __name__ == '__main__':
    events_list = []
    shifts = []
    total_time = {}
    minutes_by_shift = {}
    guards = set()
    with open("data.in", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        for line in lines:
            date = line[:line.find("]")+1][1:-1]
            action = line[line.find("]")+2:].split(" ")
            events_list.append(Event(date, action))
    events_list.sort()
    for x in events_list:
        if 'Guard' in x.action:
            alist = []
            for y in events_list[events_list.index(x)+1:]:
                if 'Guard' in y.action:
                    break
                else:
                    alist.append(y)
            shifts.append(Shift(x.action[1], alist))
    for s in shifts:
        total_time[s.guard] = 0
    for s in shifts:
        total_time[s.guard] += s.total()
        guards.add(s.guard)
    for m in range(60):
        for g in guards:
            minutes_by_shift[(g, m)] = 0
    most = sorted(total_time.items(), key=lambda x: x[1], reverse=True)[0][0]
    for g in guards:
        for m in range(60):
            for s in shifts:
                if g == s.guard:
                    for a, b in zip(s.events[0::2], s.events[1::2]):
                        if m in range(a.get_minutes(), b.get_minutes()):
                            minutes_by_shift[(g, m)] += 1
    a, b = sorted(minutes_by_shift.items(), key=lambda x: x[1], reverse=True)[0]
    print(int(a[0][1:])*int(a[1]))
