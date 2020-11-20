import pandas as pd 
import csv
import matplotlib
matplotlib.use('TkAgg') # change the backend for matplotlib 
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)

import tkinter as tk
from tkinter import *  #import everything from tkinter


#create pandas dataframe 
ClinicalDataDf=pd.read_csv('/Users/Vaia/Desktop/BMI_6018_Project/bmi6018_project/data/AllData.txt', delimiter='\t',error_bad_lines=False, sep='Wt', header=1 )

df=ClinicalDataDf[['gender', 'race', 'age_at_initial_pathologic_diagnosis',
'ethnicity','pathologic_stage','weight', 'height']]

df=ClinicalDataDf[['gender', 'race', 'age_at_initial_pathologic_diagnosis',
'ethnicity','pathologic_stage', 'weight', 'height']]

#Drop the first row
df= df.drop([df.index[0]])

print (df.shape)
Stage=df['pathologic_stage'].value_counts().to_dict()

del Stage ['[Discrepancy]'] 
del Stage ['[Not Available]']
print(Stage)

#print(df)

#Build a graph of stage and frequency and then embed it in a tkinter window 
def plot():
    fig=plt.figure()     # creat the maplotlib graph 
    x=Stage.keys()
    y=Stage.values()
    plt.bar(x,y)
    plt.title('Stage and Frequency')
    plt.xlabel('Pathologic Stage')
    plt.ylabel('Frequency')
    fig.set_size_inches(18.5, 10.5)
    plt.show()
    canvas= FigureCanvasTkAgg(fig, master = window)  #create the canvas on tkinter window
    canvas.draw()
    canvas.get_tk_widget().pack() 
    toolbar = NavigationToolbar2Tk(canvas,window) 
    toolbar.update() 
    canvas.get_tk_widget().pack() 
window= Tk()
window.title ('Graph on tkinter')
window.geometry("500x500")

plot_button = Button(master = window,  
                     command = plot, 
                     height = 2,  
                     width = 10, 
                     text = "Show the graph") 
plot_button.pack() 
window.mainloop() 
