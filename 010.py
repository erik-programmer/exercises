def execute(m: dict, value: str) -> str:
    for k, v in m.items():
        if isinstance(v, dict):
            t = execute(v, value)
            if t:
                return f"->{k}{t}"
        else:
            if v == value:
                return f"->{k}"
    return ""


assert execute({}, "1") == ""

assert execute({"a": "1"}, "1") == "->a"

assert execute({"a": "1"}, "2") == ""

assert execute({"a": {"c": "3"}, "b": "2"}, "2") == "->b"


assert (
    execute({"a": "1", "b": {"c1": "2", "c2": "3"}, "d": {"e": "4"}}, "3") == "->b->c2"
)

assert (
    execute({"a": "1", "b": {"c1": "2", "c2": "3"}, "d": {"e": "4"}}, "4") == "->d->e"
)

assert execute({"a": "1", "b": {"c": {"d": "2"}}}, "2") == "->b->c->d"
