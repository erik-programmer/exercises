def execute(m, abstand):
    for k, v in m.items():
        if isinstance(v, dict):
            print(f"{abstand}{k}->")
            execute(v, abstand + " ")
        else:
            print(f"{abstand}{k}->{v}")


m = {"a": 1, "b": 2, "c": {"d": {"e": 3}, "f": 5}, "w": 4}
execute(m, "")
