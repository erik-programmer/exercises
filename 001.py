#  ​Input Example: nums = [1, 1, 1, 2, 2, 3]
# ​ Expected Output: 1


def execute(nums: list[int]):
    if not nums:
        return None
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    mv = 0
    mk = 0
    for k, v in d.items():
        if mv <= v:
            mv = v
            mk = k
    return mk


assert execute([]) == None
assert execute([1, 1, 1, 2, 2, 3]) == 1
assert execute([2, 2, 5, 5, 5, 3]) == 5
assert execute([1, 1, 2, 2, 3]) == 2
assert execute([2, 2, 3, 1, 1, 4, 4, 4, 1, 1]) == 1
