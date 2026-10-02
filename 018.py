def order_weight(strng: str) -> str:
    l = strng.split(" ")
    l.sort(key=lambda n: (sum(int(s) for s in n), n))
    return " ".join(l)


assert order_weight("103 123 4444 99 2000") == "2000 103 123 4444 99"
assert (
    order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")
    == "11 11 2000 10003 22 123 1234000 44444444 9999"
)
assert order_weight("") == ""
