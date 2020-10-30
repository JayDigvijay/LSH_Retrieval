# -*- coding: utf-8 -*-
"""
This module generates the Signature Matrix from the Document Matrix, using a 
suitable minhashing function.

"""
########### IMPORT LIBRARIES AND OPEN DATABASE ################################
from Parameters import n, k, pickle_write, pickle_read, MinHash
import time
import random
start = time.time()


Doc_Matrix = pickle_read('Doc_Matrix.pickle')
Shingle_Dict = pickle_read('Shingle_Dict.pickle')

###############################################################################

def Signature_Generator ():
    ################# GENERATING SIGNATURES ###################################
    Signature_Matrix = {}
    for doc in Doc_Matrix:
        doc_sig = {}
        for i in range(1, n+1):
            doc_sig[i] = 10 * (4 ** k)
        Signature_Matrix[doc] = doc_sig
    #print(Signature_Matrix[3000]) 
    Hash = [[0,0]]
    for i in range(1, n + 1):
        A = random.randint(1,5)
        B = random.randint(1,5)
        Hash.append([A, B])
        for doc in Signature_Matrix:
            doc_sig = Signature_Matrix[doc]
            #print(doc_sig)
            for Shingle in Doc_Matrix[doc]:
                j = Shingle_Dict[Shingle]
                doc_sig[i] = min(doc_sig[i], MinHash(j, A, B))
            Signature_Matrix[doc] = doc_sig
    ###########################################################################
    
    ############# STORING SIGNATURE MATRIX ####################################
    pickle_write(Signature_Matrix, 'Signature_Matrix.pickle')
    pickle_write(Hash, 'Hash.pickle')
###############################################################################

Signature_Generator()
print('Minhashing completed in ', (time.time() - start), ' seconds')
