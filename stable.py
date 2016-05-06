from itertools import product
from random import shuffle

def stable(rankings, A, B):
    partners = dict((a, (rankings[(a, 1)], 1)) for a in A)
    is_stable = False # whether the current pairing (given by `partners`) is stable
    while is_stable == False:
        is_stable = True
        for b in B:
            is_paired = False # whether b has a pair which b ranks <= to n
            for n in range(1, len(B) + 1):
                a = rankings[(b, n)]
                a_partner, a_n = partners[a]
                if a_partner == b:
                    if is_paired:
                        is_stable = False
                        partners[a] = (rankings[(a, a_n + 1)], a_n + 1)
                    else:
                        is_paired = True
    return sorted((a, b) for (a, (b, n)) in partners.items())

A = ['tiffany','cole','will','kandyce','santi']
B = ['a','b','c','d','e']

rs = [[i+1 for i in range(5)] for j in range(5)]
for r in rs:
    shuffle(r)
    r = tuple(r)

rank = dict()
rank['cole']        = (2,4,3,5,1)
rank['kandyce']     = (4,3,2,5,1)
rank['santi']       = (2,3,4,5,1)
rank['tiffany']     = (2,3,4,1,5)
rank['will']        = (2,3,4,5,1)

rank['a']           = rs[0]
rank['b']           = rs[1]
rank['c']           = rs[2]
rank['d']           = rs[3]
rank['e']           = rs[4]

Arankings = dict(((a, rank[a][b_]), B[b_]) for (a, b_) in product(A, range(0, 5)))
Brankings = dict(((b, rank[b][a_]), A[a_]) for (b, a_) in product(B, range(0, 5)))
rankings = Arankings
rankings.update(Brankings)

print(stable(rankings, A, B))
