def execute(l: list) -> int:
    r = 0
    for n in l:
        if isinstance(n, list):
            r += execute(n)
        else:
            r += n
    return r


assert execute([]) == 0
assert execute([1, 2, 3]) == 6


assert execute([1, [2, 1], 3]) == 7


assert execute([1, [2, 1, [3, 1]], [1, 2]]) == 11

assert execute([1, [2, 1, [3, 1, [1]]], [1, 2]]) == 12
