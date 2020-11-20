import pandas as pd 
import csv
import tkinter as tk 
from tkinter import *
import pandastable
from pandastable import Table, TableModel



#create pandas dataframe 
ClinicalDataDf=pd.read_csv('/Users/Vaia/Desktop/BMI_6018_Project/bmi6018_project/data/AllData.txt', delimiter='\t',error_bad_lines=False, sep='Wt', header=1 )

EditedClinicalData=ClinicalDataDf[[ 'bcr_patient_barcode', 'histological_type','gender', 
'race', 'age_at_initial_pathologic_diagnosis',
'ethnicity',  
'pathologic_T', 'pathologic_N', 'pathologic_M', 'pathologic_stage', 'weight', 'height']]


#Group by gender
print(EditedClinicalData.groupby(['gender']).size())
print(EditedClinicalData['age_at_initial_pathologic_diagnosis'].count())

#Divide data based on Age + Gender
GroupA= EditedClinicalData.loc[(EditedClinicalData['age_at_initial_pathologic_diagnosis'] >'65') & (EditedClinicalData['gender'] == 'MALE')]
GroupB= EditedClinicalData.loc[(EditedClinicalData['age_at_initial_pathologic_diagnosis'] <'65') & (EditedClinicalData['gender'] == 'MALE')]
GroupC= EditedClinicalData.loc[(EditedClinicalData['age_at_initial_pathologic_diagnosis'] >'65') & (EditedClinicalData['gender'] == 'FEMALE')]
GroupD= EditedClinicalData.loc[(EditedClinicalData['age_at_initial_pathologic_diagnosis'] <'65') & (EditedClinicalData['gender'] == 'FEMALE')]

# Show the number of patients in each group
print (GroupA.shape)
print (GroupB.shape)
print (GroupC.shape)
print (GroupD.shape)


grouped_df= EditedClinicalData.loc[(EditedClinicalData['age_at_initial_pathologic_diagnosis'] > '65') & (EditedClinicalData['gender'] == 'MALE') | (EditedClinicalData['age_at_initial_pathologic_diagnosis'] <'65') & (EditedClinicalData['gender'] == 'MALE') | (EditedClinicalData['age_at_initial_pathologic_diagnosis'] >'65') & (EditedClinicalData['gender'] == 'FEMALE') | (EditedClinicalData['age_at_initial_pathologic_diagnosis'] <'65') & (EditedClinicalData['gender'] == 'FEMALE')]
print (grouped_df)

#Remove Not Available values in weight and height 

indexNamesW=grouped_df[ grouped_df ['weight']== '[Not Available]'].index
grouped_df.drop(indexNamesW, inplace= True)

indexNamesH=grouped_df[ grouped_df ['height']== '[Not Available]'].index
grouped_df.drop(indexNamesH, inplace= True)

#See the updated dataframe number of patients 
print (grouped_df.shape)

#See the data types in columns

#convert data types to floats for columns weight and height (some were strings)
grouped_df['weight']= grouped_df['weight'].astype(float)
grouped_df['height']= grouped_df['height'].astype(float)


# Find mean of weight and height 
def MeanWeight():
       return grouped_df[['weight']].mean()


print(MeanWeight())

def MeanHeight():
       return grouped_df[['height']].mean()

print(MeanHeight())

#Find minimum 

def MinWeight():
       return grouped_df[['weight']].min()

print (MinWeight())

def MaxWeight(): 
     return grouped_df[['weight']].max()

print (MaxWeight())



# Quartiles 

grouped_df['QuartileWeight']= pd.qcut (grouped_df['weight'], q=4, labels=False)


df=grouped_df

root = tk.Tk()
root.title('Show Quartiles')

frame = tk.Frame(root)
frame.pack(fill='both', expand=True)

pt = Table(frame, dataframe=df)
pt.show()

root.mainloop()

