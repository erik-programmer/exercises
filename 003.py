data = {
    "Math": [{"John": 3}, {"Jake": 5}, {"Jenny": 3}, {"Colin": 1}, {"Adam": 3}],
    "Sport": [{"Adam": 7}, {"Jake": 1}, {"Jenny": 12}, {"Colin": 1}, {"John": 3}],
    "English": [{"John": 3}, {"Adam": 1}, {"Jake": 7}, {"Colin": 1}, {"Jenny": 13}],
}
d = {}
for _, s in data.items():
    for st in s:
        for n, p in st.items():
            if n not in d:
                d[n] = p
            else:
                d[n] += p
l = []
for n, p in d.items():
    l.append({"name": n, "point": p})
l.sort(key=lambda st: st["point"], reverse=True)

for i, st in enumerate(l):
    print(f"{i+1}. {st["name"]} {st["point"]}")
