import itertools
from typing import Iterable


import itertools

ls = []
for i in list(itertools.product([False, True], repeat=3)):
    p = i[0]
    q = i[1]
    r = i[2]
    ls.append([*i, not(q), q and r, not(q and r),
              p or not(q and r), not(p or not(q and r)), p or q, not(q) or (p or q), not(not(q) or (p or q)), not(p or not(q and r)) and not(not(q) or (p or q))])

for row in ls:
    print(*row)
