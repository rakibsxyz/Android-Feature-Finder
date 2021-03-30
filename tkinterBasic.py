from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter
from traceReaderK9Data import readTraceAndParse as readTrace
from kmeansonk9datawithwordfinding import runKmeansAndCluster

def main():
    root = Tk()
    root.title("Android Feature Finder")
    root.geometry("1000x500")
    root.sourceFolder = ''
    root.sourceFile = ''
    root.iconbitmap(r'android.ico')

    def predictFeature():
        sourceFileForPrediction = filedialog.askopenfilename(parent=root, initialdir= "/", title='Please select a directory')
        
        if(sourceFileForPrediction):
            check = runKmeansAndCluster(sourceFileForPrediction)
            if(check):
                tkinter.messagebox.showinfo("Done Prediction", "see The feature")
        else:
             tkinter.messagebox.showinfo("Invalid", "Please Select a file")


    def chooseFile():
        root.sourceFile = filedialog.askopenfilename(parent=root, initialdir= "/", title='Please select a directory')
        srcFile = root.sourceFile
        print(srcFile)
        if(srcFile):
            if(readTrace(srcFile)):
                tkinter.messagebox.showinfo("Done Parsing", "Now You can Find your Feature")
        else:
            tkinter.messagebox.showinfo("Invalid", "Please Select a file")


    b_chooseFile = Button(root, text = "Chose File", width = 20, height = 3, command = chooseFile)
    b_chooseFile.place(x = 250,y = 50)
    b_chooseFile.width = 100


    predictButton = Button(root, text = "Predict Feature", width = 20, height = 3, command = predictFeature)
    predictButton.place(x = 450,y = 50)
    predictButton.width = 100

    root.mainloop()
    print(root.sourceFile )
if __name__ == "__main__":
    main()