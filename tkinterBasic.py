from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
import tkinter

from numpy.lib.polynomial import roots
from traceReaderK9Data import readTraceAndParse as readTrace
from KMEANSf1 import runKmeansAndCluster

def main():
    root = Tk()
    root.title("Android Feature Finder")
    root.geometry("1000x500")
    root.sourceFolder = ''
    root.sourceFile = ''
    root.iconbitmap(r'android.ico')
    root.listOfLocalFeature = []

    def predictFeature(): 
        srcFile = root.sourceFile
        clusterValue = checkButton()
        
        if(srcFile):
            if(readTrace(srcFile)):
                tkinter.messagebox.showinfo("Done Parsing", "Now You can Find your Feature")
                sourceFileForPrediction ="testCsv.csv"
                listOfWordsFeature, listFeature = runKmeansAndCluster(sourceFileForPrediction, clusterValue)
                root.listOfLocalFeature = listOfWordsFeature
                lenData = listFeature
                if(listFeature):
                    tkinter.messagebox.showinfo("Done Prediction", "see The feature")
                    print(listFeature)
                    comboboxUpdate(listFeature)
        else:
             tkinter.messagebox.showinfo("Invalid", "Please Select a file")


    def chooseFile():
        root.sourceFile = filedialog.askopenfilename(parent=root, initialdir= "/", title='Please select a directory')
        srcFile = root.sourceFile
        print(srcFile)
        if(srcFile):
            print("paisi File")
        else:
            tkinter.messagebox.showinfo("Invalid", "Please Select a file")


    def checkButton():
        print(featureInput.get())
        clusterValue = int(featureInput.get())
        return clusterValue

    def comboButtonCommand():
        feature = combo.get()
        print(root.listOfLocalFeature[int(feature)])
        words = root.listOfLocalFeature[int(feature)]
        featureWordListBox.delete(0, END)
        i=1
        for item in words:
            item = str(i) +". " + item
            featureWordListBox.insert(END,item)
            i= i+1

    
    def comboboxUpdate(data):
        combo.config(values=data)

    
    b_chooseFile = Button(root, text = "Choose File", width = 20, height = 3, command = chooseFile)
    b_chooseFile.place(x = 100,y = 50)
    b_chooseFile.width = 100


    predictButton = Button(root, text = "Predict", width = 20, height = 3, command = predictFeature)
    predictButton.place(x=100, y=150)
    predictButton.width = 100

    labelForFeatureinput = Label(root, text="Enter feature number")
    labelForFeatureinput.place(x= 255, y= 50)
    # labelForFeatureinput.pack()
    # place for feature input
    featureInput = Entry(root, width=20)
    featureInput.place(x = 255,y = 80)
    # featureInput.pack()

    # Button for feature input
    # featureButton = Button(root, text = "feature predict", width = 30, height=3, command= checkButton)
    # featureButton.place(x = 300, y= 280)

    # Combobox man
    data = ['0', '1', '1']
    combo = Combobox(root,values =data , width=20)
    combo.place(x=100, y=250)
    combo.current(2)
    # combo.pack()

    # Combo button
    comboButton = Button(root, text ='See Predicted Feature', command = comboButtonCommand)
    # comboButton.pack(pady=10)
    comboButton.place(x=100, y= 300)
    # comboButton.pack()

    featureWordListBox = Listbox(root, height=15, width=30)
    featureWordListBox.place(x=300, y=200)
    # featureWordListBox.pack()
    # featureWordLabel.pack()

    root.mainloop()
    print(root.sourceFile)
if __name__ == "__main__":
    main()