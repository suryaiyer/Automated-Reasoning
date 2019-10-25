import copy

clauses = [['P'], ['!P', 'Q'], ['!Q']]
# wumpus_world = [['!P12','B11'],['!B11'],['P12']]
wumpus_world = [['!P11'], ['!B11', 'P12', 'P21'], ['!P12', 'B11'],
                ['!P21', 'B11'], ['!B21', 'P11', 'P22', 'P31'], ['!P11', 'B21'],
                ['!P22', 'B21'], ['!P31', 'B21'], ['!B11'], ['B21'], ['!P12']]


def PL_resolution(clauses):
    new = []

    while True:
        n = len(clauses)

        pair = [(clauses[i], clauses[j]) for i in range(n) for j in range(i + 1, n)]

        # print(pair, 'pair')
        for (Ci, Cj) in pair:
            resolvents = PL_Resolve(Ci, Cj)


            if set() in resolvents:
                print('Resolution answer: True')
                return True

            if resolvents:
                new = union(resolvents, new)

        # print(new)
        # print('Clauses:',clauses)
        if is_subset(clauses, new)and len(new) < len(clauses):
            # print(clauses , len(clauses))
            # print(new, len(new), 'new')
            print('Resolution answer: False')
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
    # print('Resolve clause:', clause)
    return clause


# def remove(item, clause):
#     if isinstance(clause, str):
#         return clause.replace(item, '')
#     else:
#         return [i for i in clause if i != item]


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


print('Modus Poten Answer:')
PL_resolution(clauses)
print('')


print('Wumpus World Answer:')
PL_resolution(wumpus_world)
print("")
# PL_Resolve(['P', '!Q'], ['!P', 'Q'])

# PL_Resolve(['P'], ['!P'])


# Horn Clauses: Mythical = Myt
#             Immortal = I
#             Mammal = Mam
#             Horned = H
#             Magical = Mag
# 1. Myt => I   =   !Myt V I
# 2. !Myt => !I ^ Mam   =   Myt V(!I ^ Mam) =   (Myt V !I) ^ (Myt V Mam)
# 3. I V Mam => H   =   !(I V Mam) V H  =   (!I ^ !Mam) V H  = (!I V H) ^ (!Mam V H)
# 4. H => Mag   =   !H V Mag
horned_clauses_mythical=[['!Myt', 'I'], ['Myt', '!I'], ['Myt', 'Mam'],
                ['!I','H'],['!Mam', 'H'],['!H','Mag'],['!Myt']]
print('Can the unicorn be mythical?')
PL_resolution(horned_clauses_mythical)
print("")

horned_clauses_magical = [['!Myt', 'I'], ['Myt', '!I'], ['Myt', 'Mam'],
                          ['!I', 'H'], ['!Mam', 'H'], ['!H', 'Mag'], ['!Mag']]
print('Can the unicorn be magical?')
PL_resolution(horned_clauses_magical)
print("")

horned_clauses_horned = [['!Myt', 'I'], ['Myt', '!I'], ['Myt', 'Mam'],
                ['!I','H'],['!Mam', 'H'], ['!H','Mag'],['!H']]
print('Can the unicorn be horned?')
PL_resolution(horned_clauses_horned)
