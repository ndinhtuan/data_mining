items1 = [1,2,3,4,5]
Ts1 = [
        [1,3,4],
        [2,3,5],
        [1,2,3,5],
        [2,5]
    ]

items = range(1,10)
Ts = [
     [1,2,5],
     [2,4],
     [2,3],
     [1,2,4],
     [1,3],
     [2,3],
     [1,3],
     [1,2,3,5],
     [1,2,3]
    ]
s1 = int(0.5 * len(Ts))
s = 2 
print "Transactions: {}. Probability thresh: {}".format(Ts, s)

def init_apriori(Ts, s):
    #return F0
    F0 = []
    counts = [0] * len(items)
    for tran in Ts:
        for i, item in enumerate(items):
            if item in tran:
                counts[i] += 1

    for i, c in enumerate(counts):
        if c >= s:
            F0.append([items[i]])
    return F0 

import copy 

def can_prune(candidate, cur_F):

    for i, item in enumerate(candidate):
        tmp = copy.deepcopy(candidate)
        tmp.pop(i) 

        if tmp not in cur_F:
            return True 
    return False 

def gen_apriori_set(cur_F):
    
    C = []
    #gen and prune 
    # gen 
    for f in cur_F :
        for i in items :
            tmp = copy.deepcopy(f)
            if i not in f:
                tmp.append(i)
                #tmp = sorted(tmp) 
                if not can_prune(tmp, cur_F):#prune
                    C.append(tmp) 
    return C

def can_join(f1, f2):

    assert len(f1) == len(f2) 
    for i in range(len(f1)-1):
        if f1[i] != f2[i]:
            return False 

    if f1[len(f1)-1] < f2[len(f1)-1]:
        return True 
    return False 

def join(f1, f2):
    assert len(f1) == len(f2) 
    re = []

    for i in range(len(f1)-1):
        re.append(f1[i])
    re.append(f1[len(f1)-1])
    re.append(f2[len(f2) - 1])
    return re

def gen_apriori_set1(cur_F):

    C = []
    #gen and prune 
    # gen 
    for f in cur_F :
        for f1 in cur_F:
            if can_join(f, f1): 
                tmp = join(f, f1)
                #tmp = sorted(tmp) 
                if not can_prune(tmp, cur_F):#prune
                    C.append(tmp)
    return C

def is_in_transaction(s, tran):

    for item in s:
        if item not in tran:
            return False 
    return True 

def apriori_algo(Ts, s, optim=True):
    # init F0
    F0 = init_apriori(Ts, s)
    print F0
    Fs = [F0]
    cur_f = F0 

    while len(cur_f) > 0:
        #Gen apriori set K + 1: Ck+1 (Candidate)
        if optim :
            C = gen_apriori_set1(cur_f) #Candidate 
        else:
            C = gen_apriori_set(cur_f)
        print "Candidate: ",C
        counts_c = [0]*len(C)
        
        for t in Ts:
            for i, candidate in enumerate(C) :
                #count(f1)++ | fi in Ck+1
                if is_in_transaction(candidate, t):
                    counts_c[i] += 1
        # delete count(fi) < s
        for i in range(len(C)):
            if counts_c[i] < s:
                C[i] = None
                
        cur_f = []
        for i in C:
            if i is not None :
                cur_f.append(i)
        if cur_f != [] :
            Fs.append(cur_f)
        print "cur_f", cur_f
    #return {Fi|i:1->k}
    return Fs 

if __name__ == "__main__":
    print apriori_algo(Ts, s, False)
    print "------------------------"
    print apriori_algo(Ts, s)
