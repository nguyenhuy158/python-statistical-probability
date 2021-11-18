import itertools
from typing import Iterable


import itertools

ls = []
for i in list(itertools.product([False, True], repeat=3)):
    p = i[0]
    q = i[1]
    r = i[2]
    ls.append([p, q, r,
               q and r, not(q and r),
               p or not(q and r), not(p or not(q and r)),
               p or q,
               not(q),
               not(q) or (p or q),
               not(not(q) or (p or q)),
               (not(p or not(q and r))) and (not(not(q) or (p or q)))
               ])
    # ls.append([p, q, r, r and q, q or p,
    #            not(q or p), (r and q) and (not(q or p))])

for row in ls:
    # print(type(row))
    row = [1 if value else 0 for value in row]
    # print('.'.join(row))
    print(*row)
