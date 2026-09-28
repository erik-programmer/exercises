def execute(s):
    stack = []
    for i, e in enumerate(s):
        if (e == "(") or (e == "["):
            stack.append(e)
        else:
            if e == ")" and stack[-1] != "(":
                return False
            elif e == "]" and stack[-1] != "[":
                return False
            stack.pop()
    return not stack


assert execute("(]") == False
assert execute("()") == True
assert execute("(()())") == True
assert execute("(()(])") == False
assert execute("([])") == True
assert execute("([((()))])") == True
assert execute("([(]))") == False
assert execute("([(()])") == False
