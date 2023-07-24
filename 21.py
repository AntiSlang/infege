def f(x, y, h, pr1, pr2):
    s = x + y
    if (h == 5 and s < 106) or (h not in [3, 5] and s >= 106):
        return 0
    if h in [3, 5] and s >= 106:
        return 1
    if h % 2 == 0:
        moves = [f(x + 1, y, h + 1, pr1, 0), f(x + 3, y, h + 1, pr1, 1), f((x * 2) + 1, y, h + 1, pr1, 2), f(x * 3, y, h + 1, pr1, 3),
                 f(x, y + 1, h + 1, pr1, 4), f(x, y + 3, h + 1, pr1, 5), f(x, (y * 2) + 1, h + 1, pr1, 6), f(x, y * 3, h + 1, pr1, 7)]
        return any([moves[i] for i in range(len(moves)) if i not in [pr1, pr2]])
    else:
        moves = [f(x + 1, y, h + 1, 0, pr2), f(x + 3, y, h + 1, 1, pr2), f((x * 2) + 1, y, h + 1, 2, pr2), f(x * 3, y, h + 1, 3, pr2),
                 f(x, y + 1, h + 1, 4, pr2), f(x, y + 3, h + 1, 5, pr2), f(x, (y * 2) + 1, h + 1, 6, pr2), f(x, y * 3, h + 1, 7, pr2)]
        return all([moves[i] for i in range(len(moves)) if i not in [pr1, pr2]])


for y in range(1, 93):
    if f(13, y, 1, -1, -1):
        print(y)
