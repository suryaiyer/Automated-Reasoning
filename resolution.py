clauses = [['P'], ['!P', 'Q'],['!Q']]


def PL_resolution(clauses):
    new = set()
    new_clauses = set()
    clause_pair = []

    for c in clauses:
        new_clauses.add(frozenset(c))
    #print(new_clauses,'1')
    while True:
        n= len(clauses)
        #print(n,'2')
        for i in range(n):
            for j in range(i+1,n):
                clause_pair.append((clauses[i], clauses[j]))

        #print(clause_pair,'3')
        for (Ci, Cj) in clause_pair:
            resolvents = PL_Resolve(Ci, Cj)
            if resolvents==[]:
                print('True')
                return True
            new= new.union(set(resolvents))
        #print(new)
        if new.issubset(new_clauses):
            print('False')
            return False

        new_clauses = new_clauses.union(new)
    #print(resolvents)


def PL_Resolve(Ci, Cj):
    new_clause = []

    for i in Ci:
        for j in Cj:
            if (i == '!' + j) or (j == '!' + i):
                new_clause = list(set(removeall(i, Ci) +
                                removeall(j, Cj)))
    return new_clause


def removeall(item, clause):
    if isinstance(clause, str):
        return clause.replace(item, '')
    else:
        return [i for i in clause if i != item]


PL_resolution(clauses)
