from itertools import combinations


points = [(1,2), (1,4), (2,2), (2,4), (8,9)]


def check_rec(comb):
    ys = set()
    for comb in combinations(comb, 2):
        point1 = comb[0]
        point2 = comb[1]
        if point1[1] == point2[1]:
            if point1[1] not in ys:
                ys.add(point1[1])
    if len(ys) == 2:
        return True
    else:
        return False


def n_recs(points):
    n_points = len(points)
    count = 0
    for comb in combinations(points, 4):
        if check_rec(comb):
            count+=1
    print(count)
n_recs(points)