## Common Data Mining Algorithm 

### 1.Apriori Algorithm 

This algorithm is used for mining transaction database. It can be obtaned knowledge about what items are bought at same time by a customer.
I follow http://www.mathcs.emory.edu/~cheung/Courses/584-StreamDB/Syllabus/10-Mining/Apriori.html to speed up algorithm 

Apriori Algorithm consist of 3 phase: 
1. Generate candidate set Ck 
2. Counting each set c in Ck on transitions T 
3. Remove set c not bigger than supmin  

Phase 1 :
With phase 1 we can Brute Force generate all possible candidate with : add any item haven't been in set. -> Gen big candidate 
But that way is slow, I have gennerate with self-join of Ck-1: F1, F2 in Ck-1, F1 can join F1 if and only if first  k-2 item of F1 and F2 are same.

Phase 2: 
We can loop all possible transaction and all possible candidate and increase counter when see each candidate in each transaction but it need so much computation. 
So we can use hash-tree to save candidate in hash-tree and then generate k-subsets of transaction, from that use each subsets to increase counter of candidate sets

Step1: Build sub-transaction of origin transaction 
Step2: Build hash-tree include Candidate set 
Step3: Iterating over all sub-transaction on hash-tree, and increate counter of canidate sub-transaction visit.
