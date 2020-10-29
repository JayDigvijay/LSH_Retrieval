# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 08:36:42 2020

@author: Digvijay Singh

"""
import pickle
from itertools import product
from Parameters import k

#############GETTING SEQUENCE AND CLASS LISTS##################################
og_data = open('human_data.txt')
lines = og_data.readlines()

sequence_list = []
category_list = []
for line in lines:
    l = line.split('\t')
    sequence_list.append(l[0])
    category_list.append(l[1])
###############################################################################

#############CLEANING GENE SEQUENCE############################################    
gene_list = []
for gene in sequence_list:
    gene_string = str(gene)
    if gene_string == 'sequence':
        continue
    gene_string = gene_string.replace('N', '')
    gene_list.append(gene_string)
###############################################################################

#############GENERATE DOCUMENT MATRIX#################################################
Doc_Matrix = {}
doc = {}
doc_num = 1
for sequence in gene_list:
    #doc.clear()
    doc = {}
    for i in range(len(sequence)-k + 1):
        shingle = sequence[i:i+k]
        doc[shingle] = 1
    Doc_Matrix[doc_num] = doc
    doc_num += 1
###############################################################################

###################SHINGLE SEQUENCE############################################
    
Combinations = list(product(['A', 'G','C', 'T'], repeat = k))
nochar = ''
Shingle_Dict = {}
for j in range(len(Combinations)):
    S = nochar.join(Combinations[j])
    Shingle_Dict[S] = j+1
###############################################################################    
    
###################STORING AS PICKLE###########################################

pickfile = open('Document_Matrix.pickle', 'wb')
pickle.dump(Doc_Matrix, pickfile, protocol=pickle.HIGHEST_PROTOCOL)
pickfile.close()

with open('Sequence_List.pickle', 'wb') as fh:
   pickle.dump(gene_list, fh, protocol=pickle.HIGHEST_PROTOCOL)

pickfile = open('Shingle_List.pickle', 'wb')
pickle.dump(Shingle_Dict, pickfile, protocol=pickle.HIGHEST_PROTOCOL)
pickfile.close()