def execute(s: str) -> bool:
    s2 = "".join(list(l for l in s.lower() if s.isalpha()))
    return s2 == s2[::-1]


assert execute("abba") == True
assert execute("aba") == True
assert execute("abbca") == False
assert execute("abb,a.") == True
assert execute("abBa") == True
