#EX1

#p->q

# T T T
# T F F 
# F T T 
# F F T

#a
def lImplies(p,q):
    if p:
        return q
    return True    
print(lImplies(False, False))

#b
# T T T
# T F F
# F T F 
# F F F
def lAnd(p,q):
    if p:
        return q
    return False    
print(lAnd(True,False))

#c
# T T T
# T F T 
# F T T 
# F F F
def lOr(p,q):
    if p:
        return True
    if p==q:
        return False   
    return True     
print(lOr(False,False))

#d
# T T F
# T F T
# F T T 
# F F F
def lXor(p,q):
    if p==q:
        return False
    return True
print(lXor(False,False))        

#e
# T F
# F T
def lNot(p):
    if p:
        return False 
    return True
print(lNot(False)) 

#f
# T T T
# T F F 
# F T F 
# F F T
def lEquipvalent(p,q):
    if p==q:
        return True
    return False 
print(lEquipvalent(True,False))        
print('-------------------------------------------------------------------------------------')
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

#EX2

P=[True,True,False,False]
Q=[True,False,True,False]

#a
def lLImplies(P,Q):
    R = []
    for p,q in zip(P, Q):
        R.append(lImplies(p,q))
    return R
print(lLImplies(P,Q))

#b
def lLAnd(P,Q):
    R = []
    for p,q in zip(P, Q):
        R.append(lAnd(p,q))
    return R    
print(lLAnd(P,Q))

#c
def lLor(P,Q):
    R = []
    for p,q in zip(P, Q):
        R.append(lOr(p,q))
    return R 
print(lLor(P,Q))

#d
def lLXor(P,Q):
    R = []
    for p,q in zip(P, Q):
        R.append(lXor(p,q))
    return R 
print(lLXor(P,Q))  

#e
def lLNot(P):
    R = []
    for p in zip(P):
        R.append(lNot(p))
    return R
print(lLNot(P))

#f
def lLEquipvalent(P,Q):
    R = []
    for p,q in zip(P,Q):
        R.append(lEquipvalent(p,q))
    return R
print(lLEquipvalent(P,Q))        
print('-------------------------------------------------------------------------------------')

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------


#EX3: build a truth table for a statement form
#find possible combinations of statement variable
#(p->q)->r

import itertools

table = itertools.product([True, False],repeat=3)

print( 'p\tq\tr')
print('-'*20)
for p,q,r in table:
    p_imp_q = lImplies(p,q)
    p_imp_q_imp_r = lImplies(p_imp_q, r)
    print(p, '\t' , q, '\t' , r, '\t', p_imp_q, '\t', p_imp_q, '\t', p_imp_q_imp_r)
print('-------------------------------------------------------------------------------------')

#EX4
# p v q -> p ^ q -> ~p V ~q
import itertools

table = itertools.product([True,False],repeat=3)
print('p\tq\tr')
print('-'*20)
for p,q,r in table:
    p_or_q = lOr(p,q)
    p_and_q = lAnd(p,q)
    notp_or_notq = lOr(p_or_q,p_and_q)
    print(p, '\t' , q, '\t' , r, '\t', p_or_q, '\t',p_and_q, '\t', notp_or_notq)

# ~p V (q^r) -> r    
import itertools

table = itertools.product([True,False],repeat=3)
print('p\tq\tr')
print('-'*20)
for p,q,r in table:
    Np = lNot(p)
    q_and_r = lAnd(q,r)
    qr_or_Np = lOr(Np,q_and_r)
    qr_or_Np_imp_r = lImplies(qr_or_Np,r)
    print(p, '\t' , q, '\t' , r, '\t', Np, '\t',q_and_r, '\t', qr_or_Np, '\t', qr_or_Np_imp_r)

# (p → q) ∧ (q → r)
import itertools

table = itertools.product([True,False],repeat=3)
print('p\tq\tr')
print('-'*20)
for p,q,r in table:
    p_imp_q = lImplies(p,q)
    q_imp_r = lImplies(q,r)
    p_imp_q_and_q_imp_r = lImplies(p_imp_q,q_imp_r)
    print(p, '\t' , q, '\t' , r, '\t', p_imp_q, '\t',q_imp_r, '\t', p_imp_q_and_q_imp_r)

# (p ∨ (q ∧ r)) ↔ ((p ∨ q) ∧ (p ∨ r))
import itertools

table = itertools.product([True,False],repeat=3)
print('p\tq\tr')
print('-'*20)
for p,q,r in table:
    q_and_r = lAnd(q,r)
    p_or_p_and_r = lOr(p,q_and_r)
    p_or_q = lOr(p,q)
    p_or_r = lOr(p,r)
    p_or_q_and_p_or_r = lAnd(p_or_q,p_or_r)
    n = lEquipvalent(p_or_p_and_r,p_or_q_and_p_or_r)
    print(p, '\t' , q, '\t' , r, '\t', p_or_p_and_r, '\t',p_or_q_and_p_or_r, '\t', n)

# p ∨ q → ¬r ∨ t
import itertools

table = itertools.product([True,False],repeat=4)
print('p\tq\tr\tt')
print('-'*20)
for p,q,r,t in table:
    p_and_q = lAnd(p,q)
    Nr = lNot(r)
    Nr_and_t = lAnd(Nr,t)
    n = lImplies(p_and_q,Nr_and_t)
    print(p, '\t' , q, '\t' , r, '\t', t, '\t',p_and_q, '\t', Nr_and_t, '\t', n)

# p ∨ t → q → (r → t)
import itertools

table = itertools.product([True,False],repeat=4)
print('p\tq\tr\tt')
print('-'*20)
for p,q,r,t in table:
    p_and_t = lAnd(p,t)
    p_and_t_imp_q = lImplies(p_and_t,q)
    r_imp_t = lImplies(r,t)
    n = lImplies(p_and_t_imp_q,r_imp_t)
    print(p, '\t' , q, '\t' , r, '\t', t, '\t',p_and_t, '\t', p_and_t_imp_q, '\t', n)

# (p ∨ (q ∧ r)) ↔ (((p ∨ q) ∧ (p ∨ r)) ∧ (t ∨ ¬t))
import itertools

table = itertools.product([True,False],repeat=4)
print('p\tq\tr\tt')
print('-'*20)
for p,q,r,t in table:
    q_and_r = lAnd(q,r)
    p_or_q_and_r = lOr(p,q_and_r)
    p_or_q = lOr(p,q)
    p_or_r = lOr(p,r)
    Nt =lNot(t)
    t_or_Nt = lOr(t,Nt)
    a = lAnd(p_or_q,p_or_r)
    b = lAnd(a,t_or_Nt)
    n = lEquipvalent(p_or_p_and_r,b)
    print(p, '\t' , q, '\t' , r, '\t', t, '\t',p_or_q_and_r, '\t', b, '\t', n)

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------


#EX6
#a
import itertools

table = list(itertools.product([True,False],repeat = 4))

print("p\tq\tr\ts\tp->r\t~p->q\tq->s\t~r->s")
print("-"*80)
for p,q,r,s in table:
    premise1 = lImplies(p,r)
    premise2 = lImplies(lNot(p),q)
    premise3 = lImplies(q,s)
    conclusions = lImplies(lNot(r),s)
    if premise1 and premise2 and premise3:
        print(p, '\t' , q, '\t' , r, '\t',s ,'\t',premise1, '\t',premise2, '\t',premise3,'\t',conclusions,'\tCritical row')
        if not conclusions:
            print('Invalid')
            break
    else:
        print(p, '\t' , q, '\t' , r, '\t',s ,'\t',premise1, '\t',premise2, '\t',premise3,'\t',conclusions)        
print('Valid')
#ex6-b
print("+caub)")
print('-'*30) 

table = list(itertools.product([True, False], repeat=5))

print("p\tq\tr\ts\tt\tp->(q->r)\tp v s\tt->q\t~s\t~r->~t")
print("-"*75)
for p, q, r, s,t in table:
	p1 = lImplies(p,lImplies(q, r))
	p2 = lOr(p, s)
	p3 = lImplies(t, q)
	p4 = not s
	conclussion = lImplies(not r, not t)
	if p1 and p2 and p3 and p4:
		print(p, '\t', q, "\t", r, "\t", s,'\t', t, '\t', p1, "\t\t", p2, "\t", p3, "\t", p4, '\t' ,conclussion, '\t'"Critical row") 
		if not conclussion:
			print("INVALID")
			break	
			
	else:
		print(p, '\t', q, "\t", r, "\t", s,'\t', t, '\t', p1, "\t\t", p2, "\t", p3, "\t", p4, '\t' ,conclussion) 
print("VALID")


print("+ Cau c)")

table = list(itertools.product([True, False], repeat=4))

print("p\tq\tr\ts\tp->q\t~r v s\tp v r\t~q->s")
print("-"*75)
for p, q, r, s in table:
	p1 = lImplies(p, q)
	p2 =lOr(not r, s)
	p3 = lOr(p, r)
	conclussion = lImplies(not q, s)
	if p1 and p2 and p3:
		print(p, '\t', q, "\t", r, "\t", s,'\t', p1, "\t", p2, "\t", p3, "\t", conclussion, "Critical row") 
		if not conclussion:
			print("INVALID")
			break	
			
	else:
		print(p, '\t', q, "\t", r, "\t", s,'\t', p1, "\t", p2, "\t", p3, "\t", conclussion)
print("VALID")

print("+Cau d)")

table = list(itertools.product([True, False], repeat=4))

print("p\tq\tr\ts\tp->r\tp->(q v ~r)\t~q v ~s")
print("-"*75)
for p, q, r, s in table:
	p1 = s
	p2 =lImplies(p, r)
	p3 = lImplies(p, lOr(q, not r))
	p4 = lOr(not q, not s)
	conclussion = s
	if p1 and p2 and p3:
		print(p, '\t', q, "\t", r, "\t", s,'\t', p2, "\t", p3, '\t\t',p4,"\t", "Critical row") 
	if not conclussion:
		print("INVALID")
		break	
			
	else:
		print(p, '\t', q, "\t", r, "\t", s,'\t', p2, "\t", p3, '\t\t',p4)
print("VALID")
