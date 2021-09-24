def ithCombine(p, q):
	return 'if {}, then {}'.format(p, q)


def panqCombine(p, q):
	return '{} and {} not {}'.format(p, q[: q.find(" ")], q[q.find(" ") + 1:])


def npoqCombine(p, q):
	return '{} not {}, or {}'.format(p[: p.find(" ")], p[p.find(" ") + 1:], q)


p = 'it sunny'
q = 'I go camping'
print(ithCombine(p, q))
print(panqCombine(p, q))
print(npoqCombine(p, q))
