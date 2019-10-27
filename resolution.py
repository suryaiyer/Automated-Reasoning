import copy
from CNF_converter import toCNF


# Check the resolution
def PL_resolution(KB, a):
    new = []
    clauses = KB
    clauses.append(a)
    while True:
        n = len(clauses)

        pair = [(clauses[i], clauses[j]) for i in range(n) for j in range(i + 1, n)]

        for (Ci, Cj) in pair:
            resolvents = PL_Resolve(Ci, Cj)

            if set() in resolvents:
                print('Resolution answer: True')
                return True

            if resolvents and len(resolvents[0]) <= max(len(Ci), len(Cj)):
                print(resolvents, min(len(Ci), len(Cj)))
                new = union(resolvents, new)

        if is_subset(clauses, new) and len(new) < len(clauses):
            print('Resolution answer: False')
            return False

        for clause in new:
            if clause not in clauses:
                clauses.append(clause)
        new = []


def PL_Resolve(Ci, Cj):
    clause = []

    for i in Ci:
        for j in Cj:
            if (i == '!' + j) or (j == '!' + i):
                clause_set = unique(remove(i, set(Ci)), remove(j, set(Cj)))
                copy_clause_set = copy.deepcopy(clause_set)
                if len(clause_set) > 1:
                    for item1 in copy_clause_set:
                        for item2 in copy_clause_set:
                            if item1 != item2 and (item1 == '!' + item2 or item2 == '!' + item1):
                                clause_set = []

                    if clause_set:
                        clause.append(clause_set)
                else:
                    clause.append(clause_set)

    return clause


def remove(clause, item):
    item.remove(clause)
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
        for ls in list_set:
            if ls == s:
                check = True
        if not check:
            list_set.append(s)
    return list_set


def is_subset(list_set, subsets):
    check = False

    for subset in subsets:
        if subset in list_set:
            check = True
            break
    return check

# Horn Clauses: Mythical = Myt
#             Immortal = I
#             Mammal = Mam
#             Horned = H
#             Magical = Mag
# 1. Myt => I   =   !Myt V I
# 2. !Myt => !I ^ Mam   =   Myt V(!I ^ Mam) =   (Myt V !I) ^ (Myt V Mam)
# 3. I V Mam => H   =   !(I V Mam) V H  =   (!I ^ !Mam) V H  = (!I V H) ^ (!Mam V H)
# 4. H => Mag   =   !H V Mag

# PL_resolution(doors, ['W'])
