def execute(l: list[str]) -> list[list[str]]:
    if not l:
        return []
    r = [[]]
    for i, e in enumerate(l):
        r[i // 3].append(e)
        if i % 3 == 2 and i < len(l) - 1:
            r.append([])
    return r


assert execute([]) == []
assert execute(["a"]) == [["a"]]
assert execute(["a", "b"]) == [["a", "b"]]


assert execute(["a", "b", "c", "d", "e", "f"]) == [["a", "b", "c"], ["d", "e", "f"]]
assert execute(["a", "b", "c", "d", "e", "f", "g"]) == [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g"],
]
