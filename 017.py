def execute(s):
    stack = []
    for l in s:
        if stack and l == stack[-1]:
            stack.pop()
        else:
            stack.append(l)
    return "".join(stack)


assert execute("abbacad") == "cad"
assert execute("abcccb") == "abcb"
assert execute("abccb") == "a"
