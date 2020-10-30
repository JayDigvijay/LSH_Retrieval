# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:57:43 2020

@author: Prof. S.R.Singh
"""
import pickle

k = 5
b = 4
r = 25
t = 0.95
n = 100


################ MINHASH FUNCTION #############################################
def MinHash (X, A, B):
    return (A*X + B) % ((4**k))
###############################################################################


def pickle_read (file_name):
    pickfile = open(file_name, 'rb')
    var = pickle.load(pickfile)
    return var
    pickfile.close()
    
def pickle_write (var_name, file_name):
    pickfile = open(file_name, 'wb')
    pickle.dump(var_name, pickfile, protocol=pickle.HIGHEST_PROTOCOL)
    pickfile.close()
    
    
    
    
    
"""
def LD(sig1, sig2):
    if len(sig1) == 0:
        return len(t)
    if len(sig2) == 0:
        return len(sig1)
    if sig1[-1] == sig2[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([LD(sig1[:-1], sig2)+1,
               LD(sig1, sig2[:-1])+1, 
               LD(sig1[:-1], sig2[:-1]) + cost])

    return res
def Levenshtein_Similarity(sig1, sig2):
    d = list(set(sig1)|set(sig2))
    return (1 - LD(sig1, sig2)/d)
"""