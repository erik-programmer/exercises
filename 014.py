def execute(m, l):
    r = []
    for lesson in l:
        r += m[lesson]
    return [min(r), max(r)]


assert execute(
    {
        "Lesson A": [8, 9],
        "Lesson B": [7, 8],
        "Lesson C": [10, 11],
        "Lesson D": [12, 14],
        "Lesson E": [12, 13],
    },
    ["Lesson A", "Lesson B"],
) == [7, 9]


assert execute(
    {
        "Lesson A": [8, 9],
        "Lesson B": [7, 8],
        "Lesson C": [10, 11],
        "Lesson D": [12, 14],
        "Lesson E": [12, 13],
    },
    ["Lesson A", "Lesson B", "Lesson D"],
) == [7, 14]


assert execute(
    {
        "Lesson A": [8, 9],
        "Lesson B": [7, 8],
        "Lesson C": [10, 11],
        "Lesson D": [12, 14],
        "Lesson E": [12, 13],
    },
    ["Lesson A", "Lesson E"],
) == [8, 13]
