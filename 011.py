def copy(m: dict, d: dict):
    for k, v in m.items():
        if k not in d:
            d[k] = v
        else:
            d[k] += v


def execute(m1: dict, m2: dict) -> dict:
    d = {}
    copy(m1, d)
    copy(m2, d)
    return d


assert execute({}, {}) == {}

assert execute({}, {"a": 1}) == {"a": 1}

assert execute({"a": 1}, {}) == {"a": 1}

assert execute({"c": 1, "b": 3}, {"a": 1, "b": 2}) == {"b": 5, "a": 1, "c": 1}
