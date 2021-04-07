from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
import tkinter
import time
from tkinter import ttk

from numpy.lib.polynomial import roots
from GemTraceReader import readTraceAndParse as readTrace
from KMEANSf2Version import runKmeansAndCluster

def main():
    root = Tk()
    root.title("Android Feature Finder")
    root.geometry("850x500")
    root.sourceFolder = ''
    root.sourceFile = ''
    root.iconbitmap(r'android.ico')
    root.listOfLocalFeature = []

    def predictFeature(): 
        # step()
        # root.update_idletasks()
        srcFile = root.sourceFile
        clusterValue = checkButton()
        # playAnimation()
        print("ekhane")
        # time.sleep(5)
        root.update()
        print("after 5")
        if(srcFile):
            
            if(readTrace(srcFile)):
               
                
                # tkinter.messagebox.showinfo("Done Parsing", "Now You can Find your Feature")
                sourceFileForPrediction ="testCsv.csv"
                listOfWordsFeature, listFeature = runKmeansAndCluster(sourceFileForPrediction, clusterValue)
                root.listOfLocalFeature = listOfWordsFeature
                lenData = listFeature
               
                if(listFeature):
                    # stop()
                    tkinter.messagebox.showinfo("Process done", "Choose a feature to see feature words")
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
            if(i == 6):
                break

    
    def comboboxUpdate(data):
        combo.config(values=data)

    # def step():
    #     progressBar.start(10)

    # def stop():
    #     progressBar.stop()
    def playAnimation():
        for i in range(2):
            for j in range(8):
                Label(root, bg="#FFBD09", width=2, height=1).place(x=(j+22)*22,y=50)
                time.sleep(0.06)
                root.update_idletasks()
                Label(root, bg= "#1F2732", width=2, height=1).place(x=(j+22)*22,y = 50)

        # else:
        #     root.destroy()

    b_chooseFile = Button(root, text = "Choose File", width = 20, height = 3, command = chooseFile,bg='#bae3e0')
    b_chooseFile.place(x = 100+100,y = 50)
    b_chooseFile.width = 100


    predictButton = Button(root, text = "Find Feature", width = 20, height = 3, command = predictFeature,bg='#bae3e0')
    predictButton.place(x=100+100, y=150)
    predictButton.width = 100

    labelForFeatureinput = Label(root, text="Enter feature number")
    labelForFeatureinput.place(x= 255+100, y= 50)
    # labelForFeatureinput.pack()
    # place for feature input
    featureInput = Entry(root,width=13, font=('Ubuntu', 14))
    featureInput.place(x = 255+100,y = 70)
    # featureInput.pack()

    # Button for feature input
    # featureButton = Button(root, text = "feature predict", width = 30, height=3, command= checkButton)
    # featureButton.place(x = 300, y= 280)

    # Combobox man
    labelForFeatureNoLabel = Label(root, text="Choose a feature")
    labelForFeatureNoLabel.place(x=100+100, y=240)

    data = ['0']
    combo = Combobox(root,values =data , width=20)
    combo.place(x=100+100, y=250+10)
    combo.current(0)
    # combo.pack()

    # Combo button
    comboButton = Button(root, text ='See words', bg='#bae3e0',command = comboButtonCommand)
    # comboButton.pack(pady=10)
    comboButton.place(x=100+100+30, y= 300)
    # comboButton.pack()

    featureWordListBox = Listbox(root, height=15, width=30)
    featureWordListBox.place(x=300+100, y=200)
    # featureWordListBox.pack()
    # featureWordLabel.pack()

    labelForFeaturewords = Label(root, text="Feature Words")
    labelForFeaturewords.place(x=300+100, y=180)

    labelFortool = Label(root, text="Android Feature Finder",font=('Ubuntu', 14))
    labelFortool.place(x=580, y=20)


    # Progress bar
    # progressBar = ttk.Progressbar(root, orient=HORIZONTAL,
    #     length=200, mode= 'determinate')
    # progressBar.place(x=580,y=50)
    # # progressBar.pack()
    

    # progressBarButton = Button(root, text="Progress", comman =step)
    # progressBarButton.pack(pady=30)

    # stopButton = Button(root, text="stop", command=stop)
    # stopButton.pack(pady=30)

    # Label(root, 
    #     bg="black", fg="#FFBD09").place(x=600,y=50)

    # for i in range(16):
    #     Label(root, bg="#1F2732", width=2, height=1).place(x=(i+22))

    # root.update()
   
    root.mainloop()
    print(root.sourceFile)
if __name__ == "__main__":
    main()
