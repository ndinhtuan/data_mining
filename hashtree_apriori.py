import copy 

# tran is transaction (tuple) include sequence items
# return k-subsets of transaction 
def gen_subtransaction(cur_set, remain_set, remain_lenset, subsets):
    
    if remain_lenset == 0:
        subsets.append(cur_set)
    
    assert len(remain_set)-(remain_lenset-1) >= 0 
    candidate_items = remain_set[:len(remain_set)-(remain_lenset-1)+1]

    for i, item in enumerate(candidate_items): 
        tmp_cur_set = copy.deepcopy(cur_set)
        tmp_cur_set.append(item) 
        tmp_remain_set = remain_set[i+1:]
        gen_subtransaction(tmp_cur_set, tmp_remain_set, remain_lenset-1, subsets)

class Node(object):

    def __init__(self):
        self.bucket = dict()
        #self.counters = [] # counter for each candidate
        self.child = [None] * 3


class HashTreeApriori(object):
    
    def __init__(self, candidates):
        self.candidates = candidates 
        self.root = Node() 
        self.create_hash_tree()

    def create_hash_tree(self):
        
        for c in candidates: 
            print "Adding {}".format(c)
            self.add_candidate(c, copy.deepcopy(c), self.root)

    def add_candidate(self, remain_set, candidate, root):

        hash_val = remain_set.pop(0)%3

        if root.child[hash_val] is None :
            root.child[hash_val] = Node()

        if len(remain_set) == 0:
            root.child[hash_val].bucket["{}".format(candidate)] = 0
            return 
        #else:
        #    if len(remain_set) == 0:
        #        root[hash_val].bucket["{}".format(candidate)] = 0

        self.add_candidate(remain_set, candidate, root.child[hash_val])

    def check_transaction(self, tran):

        tmp = copy.deepcopy(tran) 
        cur_node = self.root 

        while len(tmp) > 1:

            hash_val = tmp.pop(0)%3
            cur_node = cur_node.child[hash_val]

        cur_node.bucket["{}".format(tran)] += 1 

    def get_frequent_sets(self, minsup, root, sets):
        
        if root.child == [None, None, None]:
            for key in root.bucket.keys():
                if root.bucket[key] >= minsup:
                    sets.append(key)
            return 

        for i in range(len(root.child)):
            if i is not None:
                self.get_frequent_sets(minsup, root.child[i], sets)

    def show_bucket(self, root):

        if root.child == [None, None, None]:
            print root.bucket.keys() 
            print "-----------------"
            return 

        for i in range(len(root.child)):
            if root.child[i] is not None :
                print "Branch {} :".format(i)
                self.show_bucket(root.child[i])

if __name__ == "__main__":

    transaction = [1,2,3,4,5]
    lensubset = 3 
    subsets = [] 
    gen_subtransaction([], transaction, lensubset, subsets)
    print subsets
    
    candidates = [
            [1,2,4],
            [1,2,5],
            [1,3,6],
            [1,4,5]
            ]
    hash_tree = HashTreeApriori(candidates)
    hash_tree.show_bucket(hash_tree.root)
