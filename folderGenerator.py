# Program: folderGenerator.py
# Author: Justin Mau
# Date: 2/2/2023

# --------------
import os
import csv
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# ------------------------------------
window = Tk()
window.title('Folder Generator')

classFolder = StringVar()
classlistFile = StringVar()
assignmentType = StringVar()
assignmentCount = IntVar()



# define button click functions
def selectClassFolder():
    dir = filedialog.askdirectory()
    classFolder.set(dir)
    
def selectClasslist():
    file = filedialog.askopenfilename()
    classlistFile.set(file)
    
def createFolders():
    # sets the working directory to the class folder
    os.chdir(classFolder.get())

    # reads in the classlist
    classlist = []
    with open(classlistFile.get(), mode = 'r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            classlist.append((line[0] + line[1]).strip(" "))

    for i in range(int(assignmentCount.get())):
        # creates a directory assignment
        os.mkdir(assignmentType.get() + str(i + 1))   
        # changes directory to that new folder
        os.chdir(os.getcwd() + f"/{assignmentType.get()}{str(i + 1)}")
        
        # goes through the classlist and creates a folder for each student
        for student in classlist:
            os.mkdir(student)
                
        os.chdir(os.getcwd() + "/../")
    
    # updates status and resets fields    
    messagebox.showinfo("Message", "All done!")
    classFolder.set("")
    classlistFile.set("")
    assignmentType.set("")
    assignmentCount.set(0)

    
    
# creating all the display elements
label_classFolder = Label(text="Class Folder: ")
entry_classFolderPath = Entry(window, textvariable = classFolder)
button_explore1 = Button(window,
                        text = "Browse Folders",
                        command = selectClassFolder)

label_classlist = Label(text="Classlist: ")
entry_classlistFile = Entry(window, textvariable = classlistFile)
button_explore2 = Button(window,
                        text = "Browse Files",
                        command = selectClasslist)

label_assignmentType = Label(text="Assignment Type (Lab, Project, etc): ")
entry_assignmentType = Entry(window, textvariable = assignmentType)

label_assignmentCount = Label(text="Number of Assignments: ")
entry_assignmentCount = Entry(window, textvariable = assignmentCount)

button_createFolders = Button(window,
                                text = "Create Folders",
                                command = createFolders)



# Sets the elements to the basic grid
label_classFolder.grid(column=1, row=1)
entry_classFolderPath.grid(column=2, row=1)
button_explore1.grid(column = 3, row = 1)

label_classlist.grid(column=1, row=2)
entry_classlistFile.grid(column=2, row=2)
button_explore2.grid(column = 3, row = 2)

label_assignmentType.grid(column=1, row=3)
entry_assignmentType.grid(column=2, row=3)

label_assignmentCount.grid(column=1, row=4)
entry_assignmentCount.grid(column=2, row=4)

button_createFolders.grid(column=4, row=5)


# -----------
window.mainloop()            
