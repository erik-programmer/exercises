def execute(m: dict) -> int:
    r = 0
    for k, v in m.items():
        if isinstance(v, dict):
            t = execute(v)
            if t > r:
                r = t
        else:
            if v > r:
                r = v
    return r


print(execute({"a": 2, "b": {"c1": 3, "c2": 2}, "d": {"e": 2}}))

assert execute({}) == 0

assert execute({"a": 1}) == 1

assert execute({"a": 2, "b": {"c1": 2, "c2": 3}, "d": {"e": 2}}) == 3

assert execute({"a": 1, "b": {"c": {"d": 3}}}) == 3
