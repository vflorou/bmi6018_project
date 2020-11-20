import pandas as pd 
import csv
import tkinter as tk 
from tkinter import *
import pandastable
from pandastable import Table, TableModel

#read_file=pd.read_csv (r'/Users/Vaia/Desktop/BMI_6018_Project/bmi6018_project/data/AllData.txt', error_bad_lines=False)
#skip bad lines 
#read_file.to_csv (r'/Users/Vaia/Desktop/BMI_6018_Project/bmi6018_project/data/ClinicalData.csv')

#create pandas dataframe 
ClinicalDataDf=pd.read_csv('/Users/Vaia/Desktop/BMI_6018_Project/bmi6018_project/data/AllData.txt', delimiter='\t',error_bad_lines=False, sep='Wt', header=1 )

#see the shape of the DF (columns and rows)
print(ClinicalDataDf.shape)

#See the columns of the DF
print(ClinicalDataDf.columns,  sep="\n")

#Edit the columns of the dataframe
EditedClinicalData=ClinicalDataDf[[ 'bcr_patient_barcode', 'histological_type','gender', 
'race', 'age_at_initial_pathologic_diagnosis',
'ethnicity',  
'pathologic_T', 'pathologic_N', 'pathologic_M', 'pathologic_stage', 'weight', 'height']]
print(EditedClinicalData.shape)
print(EditedClinicalData.iloc[1:])

#Find the row of a particular sample identified by bcr_patient_barcode

def Findyoursample():
     your_bcr_patient_barcode=input('enter your bcr_patient_barcode:\n')
     for bcr_patient_barcode in EditedClinicalData:
         return (EditedClinicalData.loc[EditedClinicalData['bcr_patient_barcode']==your_bcr_patient_barcode])
        
# show the results in a window
df=Findyoursample()

root = tk.Tk()
root.title('Your sample')

frame = tk.Frame(root)
frame.pack(fill='both', expand=True)
frame.config(bg='green')
pt = Table(frame, dataframe=df)
pt.show()

root.mainloop()
