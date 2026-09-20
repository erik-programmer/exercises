def execute(m: dict) -> dict:
    r = {}
    for k, v in m.items():
        if isinstance(v, dict):
            r[k] = execute(v)
        else:
            r[k] = v
    return r


assert execute({}) == {}
assert execute({"a": 1}) == {"a": 1}


m1 = {"a": 1, "b": {"c": {"w": {"q": 6}}}}
m2 = execute(m1)
m2["b"]["c"] = 4

assert m2["b"]["c"] == 4
assert m1["b"]["c"]["w"]["q"] == 6
