#clauses = [['P'], ['!P', 'Q'],['!Q']]
wumpus_world=[['P11'], ['!B11','P12','P21'],['!P12','B11'],['!P21','B11'],['!B21','P11','P22','P31'],['!P11','B21'],['!P11','B21'],['P22','B21'],['!P31','B21'],['!B11'],['B21'],['P12']]

def PL_resolution(clauses):
    new = set()
    new_clauses = set()
    clause_pair = []

    for c in clauses:
        new_clauses.add(frozenset(c))

    #print(new_clauses,'1')
    while True:
        n= len(new_clauses)
        #print(n,'2')
        new_clause_líst = []
        for i in new_clauses:
            new_clause_líst.append(i)

        for i in range(n):
            for j in range(i+1,n):

                clause_pair.append((new_clause_líst[i], new_clause_líst[j]))

        #print(clause_pair,'3')
        for (Ci, Cj) in clause_pair:
#            print(Ci,Cj)
            resolvents = PL_Resolve(Ci, Cj)
            #print(resolvents,'d')
            if resolvents==[]:
                print('Resolution answer: True')
                return True
            if resolvents!=['No']:
 #               print(resolvents,"here")
                new= new.union(set(resolvents))

        print(new)
        if new !=[]:
            if new.issubset(new_clauses):
                print('Resolution answer: False')
                return False

            new_clauses = new_clauses.union(new)
    #print(resolvents)


def PL_Resolve(Ci, Cj):
    new_clause = []
    print("Inside",Ci,Cj)
    for i in Ci:
        for j in Cj:
            if (i == '!' + j) or (j == '!' + i):
                list1 = remove(i, Ci)
                list2 = remove(j, Cj)
                if list1==[] and list2==[]:
                    return []
                elif list1!=[] and list2==[]:
                    return list(set(list1))
                elif list1==[] and list2!=[]:
                    return list(set(list2))
                else:
                    print(list1,list2)
                    new_clause = list(set(list1 + list2))
                return new_clause
  #  print("New_clause is ",new_clause)
    return ['No']


def remove(item, clause):
    if isinstance(clause, str):
        return clause.replace(item, '')
    else:
        return [i for i in clause if i != item]


PL_resolution(wumpus_world)
