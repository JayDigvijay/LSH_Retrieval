# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 23:02:30 2020

@author: Prof. S.R.Singh
"""
############# IMPORTING LIBRARIES AND PARAMETERS ##############################
import pickle
import random
import time
from Parameters import k, n, r, b, t

###############################################################################


############## OPENING DATABASE FILES #########################################
pickfile = open('Sequence_List.pickle', 'rb')
Sequence_List = pickle.load(pickfile)

pickfile = open('Shingle_List.pickle', 'rb')
Shingle_Dict = pickle.load(pickfile)
pickfile.close()

pickfile = open('Doc_Buckets.pickle', 'rb')
Doc_Buckets = pickle.load(pickfile)
pickfile.close()

pickfile = open('Signature_Matrix.pickle', 'rb')
Signature_Matrix = pickle.load(pickfile)
pickfile.close()
###############################################################################

############## DEFINING SIMILARITY AND HASHING FUNCTION #######################
def Jaccard_Similarity(sig1, sig2):
    Intersect = list(set(sig1) & set(sig2))
    Union = list(set(sig1) | set(sig2))
    return len(Intersect)/len(Union)

def MinHash (x, i):
    return (i*x + i) % (4**k)
###############################################################################
    
########### QUERY INPUT #######################################################
query_choice = input("Press '1' to enter your own DNA Sequence. Press '0' to choose a DNA sequence randomly from database.\n")

if(query_choice == '1'):
    query = input("Enter your query as a string of DNA sequence in uppercase, e.g. 'AGCATACG...'\n")
else:
    query = random.choice(Sequence_List)
    query_num = Sequence_List.index(query)
start = time.time() 

#print(query_num)
###############################################################################

#################### QUERY PROCESSING #########################################

############### 1.SHINGLING #################################
query_doc = {}
for i in range(len(query)-k + 1):
    shingle = query[i:i+k]
    query_doc[shingle] = 1
#############################################################

############## 2.MINHASHING #################################
query_sig = {}
for i in range(1, n+1):
        query_sig[i] = 10 * (4 ** k)

for i in range(1, n+1):
    for Shingle in query_doc:
            j = Shingle_Dict[Shingle]
            query_sig[i] = min(query_sig[i], MinHash(j,i))
#print(query_sig)
############################################################

############# 3.LSH ########################################
Candidate_List = []
for p in range (b):
        band = []
        for i in range(p*r + 1,(p+1)*r + 1):
            band.append(query_sig[i])
        bucket = 0
        for x in band:
            bucket += (p+1)*x
        if bucket in Doc_Buckets:
            Candidate_List = list(set(Doc_Buckets[bucket]) | set(Candidate_List))
#print(Candidate_List)
###############################################################################
            
############# SIMILARITY CHECKING #############################################
sig1 = []
Similar = []
for i in range (1, n+1):
    sig1.append(query_sig[i])
for doc in Candidate_List:
    sig2 = []
    for i in range (1, n+1):
        sig2.append(Signature_Matrix[doc][i])
    JC = Jaccard_Similarity(sig1, sig2)
    if(JC > t):
        Similar.append(doc)
#print(Similar)
###############################################################################
print("For the query:", query)
print((len(Similar)-1), " sequences were retrieved in ", (time.time() - start), " seconds with similarity greater than or equal to ", t*100, "% with the query.\n ")
display = input("Press '1' to view sequence numbers.\n")
if(display):
    print(Similar)
         