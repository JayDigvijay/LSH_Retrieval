# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:55:12 2020

@author: Digvijay Singh
"""
########### IMPORT LIBRARIES AND OPEN DATABASE ################################
import pickle
from Parameters import n, k
import time

start = time.time()

pickfile = open('Document_Matrix.pickle', 'rb')
Doc_Matrix = pickle.load(pickfile)

pickfile = open('Shingle_List.pickle', 'rb')
Shingle_Dict = pickle.load(pickfile)
pickfile.close()
###############################################################################

################ MINHASH FUNCTION #############################################
def MinHash (x, i):
    return (i*x + i) % (4**k)
###############################################################################

################# GENERATING SIGNATURES #######################################
Signature_Matrix = {}

for doc in Doc_Matrix:
    doc_sig = {}
    for i in range(1, n+1):
        doc_sig[i] = 10 * (4 ** k)
    Signature_Matrix[doc] = doc_sig
#print(Signature_Matrix[3000]) 
    
for i in range(1, n + 1):
    for doc in Signature_Matrix:
        doc_sig = Signature_Matrix[doc]
        #print(doc_sig)
        for Shingle in Doc_Matrix[doc]:
            j = Shingle_Dict[Shingle]
            doc_sig[i] = min(doc_sig[i], MinHash(j,i))
        Signature_Matrix[doc] = doc_sig
###############################################################################

############# STORING SIGNATURE MATRIX ########################################
pickfile = open('Signature_Matrix.pickle', 'wb')
pickle.dump(Signature_Matrix, pickfile, protocol=pickle.HIGHEST_PROTOCOL)
pickfile.close()
###############################################################################
print('Minhashing completed in ', (time.time() - start), ' seconds')
