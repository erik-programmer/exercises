def execute(m: dict, parent: str) -> list[str]:
    r = []
    for k, v in m.items():
        if isinstance(v, dict):
            r += execute(v, f"{parent}.{k}" if parent else k)
        else:
            r.append(f"{parent}.{k}" if parent else k)
    return r


assert execute({}, "") == []

assert execute({"a": "_"}, "") == ["a"]

assert execute({"a": "_", "b": {"c1": "_", "c2": "_"}, "d": {"e": "_"}}, "") == [
    "a",
    "b.c1",
    "b.c2",
    "d.e",
]

assert execute({"a": "_", "b": {"c": {"d": "_"}}}, "") == ["a", "b.c.d"]
