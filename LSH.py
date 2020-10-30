# -*- coding: utf-8 -*-
"""
This module divides the Signature Matrix into b bands with r rows each.
For each sequence, the signatures corresponding to each band are dumped into a 
bucket, with similar signatures having a higher probability of going to the same
bucket.

"""
########### IMPORT LIBRARIES AND OPEN DATABASE ################################
#from Minhashing import Signature_Matrix
from Parameters import  r, b, pickle_read, pickle_write

Signature_Matrix = pickle_read('Signature_Matrix.pickle')
###############################################################################
def Bucketing():
    '''
        Create buckets for the docs using the signature matrix
    '''
    ############ BUCKETING THE SIGNATURES #####################################
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
                
    ###########################################################################
    
    #################### STORING THE BUCKETED DOCUMENTS #######################
    pickle_write(Doc_Buckets, 'Doc_Buckets.pickle')
    ###########################################################################

Bucketing()