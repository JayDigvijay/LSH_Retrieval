# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:42:52 2020

@author: Digvijay Singh
"""
########### IMPORT LIBRARIES AND OPEN DATABASE ################################
#from Minhashing import Signature_Matrix
from Parameters import  r, b
import pickle

pickfile = open('Signature_Matrix.pickle', 'rb')
Signature_Matrix = pickle.load(pickfile)
###############################################################################

############ BUCKETING THE SIGNATURES #########################################
Doc_Buckets = {}
for doc in Signature_Matrix:
    sig = Signature_Matrix[doc]
    for p in range (b):
        band = []
        for i in range(p*r + 1,(p+1)*r + 1):
            band.append(sig[i])
        bucket = 0
        for x in band:
            bucket += (p+1)*x
        if bucket in Doc_Buckets:
            Doc_Buckets[bucket].append(doc)
        else:
            bucket_list = [doc]
            Doc_Buckets[bucket] = bucket_list
###############################################################################

#################### STORING THE BUCKETED DOCUMENTS ###########################
pickfile = open('Doc_Buckets.pickle', 'wb')
pickle.dump(Doc_Buckets, pickfile, protocol=pickle.HIGHEST_PROTOCOL)
pickfile.close()
###############################################################################