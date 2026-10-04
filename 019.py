def sum_pairs(ints, s):
    m = set()
    for n in ints:
        rest = s - n
        if rest in m:
            return [rest, n]
        m.add(n)
    return None


def sum_pairs2(ints, s):
    r = None
    last_i2 = len(ints)
    for i1, n1 in enumerate(ints):
        for i2, n2 in enumerate(ints[i1 + 1 :]):
            if n1 + n2 == s and i2 < last_i2:
                last_i2 = i2
                r = [n1, n2]
    return r


l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]
l9 = [1] * 10000000
l9[len(l9) // 2 - 1] = 6
l9[len(l9) // 2] = 7
l9[len(l9) - 2] = 8
l9[len(l9) - 1] = -3
l9[0] = 13
l9[1] = 3

assert sum_pairs(l1, 8) == [1, 7]
assert sum_pairs(l2, -6) == [0, -6]
assert sum_pairs(l3, -7) == None
assert sum_pairs(l4, 2) == [1, 1]
assert sum_pairs(l5, 10) == [3, 7]
assert sum_pairs(l6, 8) == [4, 4]
assert sum_pairs(l7, 0) == [0, 0]
assert sum_pairs(l8, 10) == [13, -3]
