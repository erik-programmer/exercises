def execute(l: list[str]) -> list[float]:
    r = []
    for w in l:
        try:
            number = float(w)
            r.append(number)
        except ValueError:
            try:
                number = float(w[0:-1])
                r.append(number)
            except ValueError:
                pass
    return r


assert execute(["12.1", "wrong", "12.2C", "12.2.2", "12"]) == [12.1, 12.2, 12]
