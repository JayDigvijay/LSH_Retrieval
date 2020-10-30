# -*- coding: utf-8 -*-
"""
This module is responsible for interacting with the user, processing the inputs 
fed by him, and fetching the results for the same, using the LSH based corpus 
generated in the previous modules. 
"""
############# IMPORTING LIBRARIES AND PARAMETERS ##############################
import time
from Parameters import k, n, t, r, MinHash, pickle_read

###############################################################################


############## OPENING DATABASE FILES #########################################
Sequence_List = pickle_read('Seq_List.pickle')
Shingle_Dict = pickle_read('Shingle_Dict.pickle')
Doc_Buckets = pickle_read('Doc_Buckets.pickle')
Signature_Matrix =  pickle_read('Signature_Matrix.pickle')
Doc_Matrix = pickle_read('Doc_Matrix.pickle')
Hash = pickle_read('Hash.pickle')

###############################################################################

############## DEFINING SIMILARITY AND HASHING FUNCTION #######################
def Jaccard_Similarity(sig1, sig2):
    '''
        Calculates Jaccard Similarity between two arrays
    '''
    Intersect = list(set(sig1) & set(sig2))
    Union = list(set(sig1) | set(sig2))
    return len(Intersect)/len(Union)

###############################################################################
def Query_Retrieval():
    '''
        Takes query input, processes input through shingling and generates its signature
        Uses the generated signature to bucket query and documents
        Using the buckets, a check for true negatives and false positives is performed, after which result is given
    '''
    ########### QUERY INPUT ###################################################
    
    query = input("Enter your query as a string of DNA sequence in uppercase, e.g. 'AGCATACG...'\n")
    query = query.replace('N', '')
    print("For the query:", query)
    #print(query_num)
    ###########################################################################
    start = time.time() 
    #################### QUERY PROCESSING #####################################
    
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
        a = Hash[i][0]
        b = Hash[i][1]
        #print(a,b)
        for Shingle in query_doc:
                j = Shingle_Dict[Shingle]
                query_sig[i] = min(query_sig[i], MinHash(j, a, b))
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
    #print(len(Candidate_List))
    ###########################################################################
                
    ############# SIMILARITY CHECKING #########################################
    sig1 = []
    Similar = {}
    for shingle in query_doc:
        sig1.append(shingle)
    
    for doc in Candidate_List:
        sig2 = []
        for shingle in Doc_Matrix[doc]:
            sig2.append(shingle)
        JC = Jaccard_Similarity(sig1, sig2)
        if(JC > t):
            Similar[doc] = Sequence_List[doc]
    """
    for doc in Candidate_List:
        sig1 = [Signature_Matrix[doc][i] for i in range (1, 101)]
        sig2 = []
        for i in range(1, 101):
            sig2.append(Signature_Matrix[doc][i])
        JC = Jaccard_Similarity(sig1, sig2)
        if(JC > t):
            Similar[doc] = Sequence_List[doc]
    """
    print("Results retrieved in", (time.time() - start), " seconds")
    return Similar
    ###########################################################################

Results = Query_Retrieval()
print((len(Results)), " sequence(s) retrieved  with similarity greater than or equal to ", t*100, "% with the query.\n ")
display = input("Press '1' to view sequences retrieved.\n")
Similar_Docs = [key for key in Results]
if(display == '1'):
    print(Similar_Docs)
while(1):
    q = int(input('Press 0 to exit, or sequence number to print the sequence\n')) 
    if q == 0:
        break
    else:
        print(Results[q])