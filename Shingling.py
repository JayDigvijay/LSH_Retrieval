# -*- coding: utf-8 -*-
"""
This file reads the sequences from given text file, cleans them of 'N' values and 
lists out all the possible k-shingles present in each sequence.

"""
from itertools import product
from Parameters import k, pickle_write

def Shingling ():
    #############GETTING SEQUENCE AND CLASS LISTS##################################
    og_data = open('human_data.txt')
    lines = og_data.readlines()
    
    sequence_list = []
    #category_list = []
    for line in lines:
        l = line.split('\t')
        sequence_list.append(l[0])
    ###############################################################################
    
    #############CLEANING GENE SEQUENCE############################################    
    gene_list = []
    for gene in sequence_list:
        gene_string = str(gene)
        if gene_string == 'sequence':
            gene_string = ''
        gene_string = gene_string.replace('N', '')
        gene_list.append(gene_string)
    ###############################################################################
    
    #############GENERATE DOCUMENT MATRIX#################################################
    Doc_Matrix = {}
    doc = {}
    doc_num = 1
    for sequence in gene_list[1:]:
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
    #print(gene_list[3357])
    pickle_write(Doc_Matrix, 'Doc_Matrix.pickle')
    pickle_write(Shingle_Dict, 'Shingle_Dict.pickle')
    pickle_write(gene_list, 'Seq_List.pickle')
    ###############################################################################
    
Shingling()