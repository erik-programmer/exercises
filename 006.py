def execute(l: list[int], n: int) -> bool:
    if not l:
        return False
    me = l[len(l) // 2]
    if n == me:
        return True
    if n > me:
        t = l[len(l) // 2 + 1 :]
        return execute(t, n)
    if n < me:
        t = l[: len(l) // 2 - 1]
        return execute(t, n)
    return False


assert execute([], 1) == False
assert execute([2, 3, 4, 5, 6, 7, 8, 9, 10], 9) == True
assert execute([2, 3, 4, 5, 6, 7, 8, 9, 10], 19) == False
assert execute([1, 3, 5, 6, 7], 5) == True
assert execute([1, 3, 5, 6, 7], 7) == True
