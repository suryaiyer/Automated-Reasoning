clauses = [['P'], ['!P', 'Q'], ['Q']]
# wumpus_world = [['!P12','B11'],['!B11'],['P12']]
wumpus_world = [['!P11'], ['!B11', 'P12', 'P21'], ['!P12', 'B11'],
                ['!P21', 'B11'], ['!B21', 'P11', 'P22', 'P31'], ['!P11', 'B21'],
                ['!P22', 'B21'], ['!P31', 'B21'], ['!B11'], ['B21'], ['!P12']]


def PL_resolution(clauses):
    new = []
    new_clauses = set()
    pair = []

    # for c in clauses:
    #     new_clauses=[frozenset(c)]

    # print(new_clauses,'1')
    while True:
        n = len(clauses)
        # print(n,'2')
        for i in range(n):
            for j in range(i + 1, n):
                pair.append((clauses[i], clauses[j]))

        # print(pair, 'pair')
        for (Ci, Cj) in pair:
            resolvents = PL_Resolve(Ci, Cj)
            # print("Resolvents:", resolvents)

            if set() in resolvents:
                print('True')
                return True

            if resolvents:
                new = union(resolvents, new)

        # print(new)
        if is_subset(clauses, new):
            print('False')
            return False

        for clause in new:
            if clause not in clauses:
                clauses.append(clause)
        new = []
    # print(resolvents)


def PL_Resolve(Ci, Cj):
    clause = []
    org_clause = [Ci, Cj]
    # print(org_clause)

    for i in Ci:
        for j in Cj:
            # print(i)
            if (i == '!' + j) or (j == '!' + i):
                clause_set = unique(remove(i, set(Ci)), remove(j, set(Cj)))
                clause.append(clause_set)
    # print(clause)
    return clause


# def remove(item, clause):
#     if isinstance(clause, str):
#         return clause.replace(item, '')
#     else:
#         return [i for i in clause if i != item]


def remove(clause='', item=set()):
    item.discard(clause)
    return item


def unique(Ci, Cj):
    unique_set = Ci
    for item in Cj:
        unique_set.add(item)
    return unique_set


def union(sets, list_set):
    list_set = list(list_set)

    for s in sets:
        check = False
        for contain_set in list_set:
            if contain_set == sets:
                check = True
        if not check:
            list_set.append(s)
    return list_set


def is_subset(list_set, subsets):
    check = False

    for subset in subsets:
        if subset in list_set:
            check = True
    return check


PL_resolution(wumpus_world)
# PL_Resolve(['P'], ['!P', 'Q'])
