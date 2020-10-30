import numpy as np
import pandas as pd

supervised_gene= pd.read_csv('data/95_genes.txt',sep='\t',header=0)
# print(supervised_gene)

clinicalinfo=pd.read.csv('data/updated_clinicalinfo.csv',sep='\t',header=0)
print(clinicalinfo)