# Program: sortSubmissions.py
# Author: Justin Mau
# Date: 2/2/2023

# --------------
import os
import csv
import shutil
from zipfile import ZipFile
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox



# ------------------------------------
window = Tk()
window.title('Sort Assignment Submissions')


classlistFile = StringVar()
assignmentFolder = StringVar()
submissionFolder = StringVar()

simplifyFilenames_Y_N = BooleanVar()


# define button click functions
def selectAssignmentFolder():
    dir = filedialog.askdirectory()
    assignmentFolder.set(dir)
    
def selectClasslist():
    file = filedialog.askopenfilename()
    classlistFile.set(file)

def selectSubmissionFolder():
    dir = filedialog.askdirectory()
    submissionFolder.set(dir)
    
def sortSubmissions():
    os.chdir(assignmentFolder.get())
    
    # reads in the classlist
    classlist = []
    with open(classlistFile.get(), mode = 'r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            classlist.append((line[0] + line[1]).strip(" "))
            
    # gets the directories for assignment folder and submissions 
    os.chdir(submissionFolder.get())

    # get all of the files in the submissions folder
    fileList = os.listdir(os.getcwd())
    

    # goes through each student, and find's all the files they submitted
    for student in classlist:
        # sets source and destination for moving files
        source = os.getcwd()
        destination = assignmentFolder.get() + f"/{student}"
        
        print(f"{student}'s Submission Contents:")
        for file in fileList:
            if (file.find(student) != -1):
                
                # if check box selected, will try to remove the D2L auto-generated name
                if (simplifyFilenames_Y_N.get() == TRUE):
                    os.rename(file, file.split(" ")[-1])
                    file = file.split(" ")[-1]

                # moves the file from 
                src_path = os.path.join(source, file)
                dst_path = os.path.join(destination, file)
                shutil.move(src_path, dst_path)
                
                print(file)
                # print(file.split(" ")[-1])
                
                # now extracts it if its a zip
                if(file.endswith(".zip")):
                    zip = ZipFile(dst_path)
                    zip.extractall(destination)
                    zip.close()
                    os.remove(dst_path) # removes that zip file 
        print("-----------------------------------")
    
    print("\n All done!")

    
    
# creating all the display elements
label_assignmentFolder = Label(text="Assignment Folder: ")
entry_assignmentFolder = Entry(window, textvariable = assignmentFolder)
button_explore1 = Button(window,
                        text = "Browse Folders",
                        command = selectAssignmentFolder)

label_classlist = Label(text="Classlist: ")
entry_classlistFile = Entry(window, textvariable = classlistFile)
button_explore2 = Button(window,
                        text = "Browse Files",
                        command = selectClasslist)

label_submissionsFolder = Label(text="Submissions Folder: ")
entry_submissionsFolder = Entry(window, textvariable = submissionFolder)
button_explore3 = Button(window,
                        text = "Browse Folders",
                        command = selectSubmissionFolder)

button_sortSubmissions = Button(window,
                                text = "Sort Submissions",
                                command = sortSubmissions)


check_rename = Checkbutton(window, 
                           text = 'Simplify file names?',
                           variable = simplifyFilenames_Y_N,
                           onvalue= TRUE, offvalue= FALSE)



# Sets the elements to the basic grid
label_classlist.grid(column=1, row=1)
entry_classlistFile.grid(column=2, row=1)
button_explore2.grid(column = 3, row = 1)

label_assignmentFolder.grid(column=1, row=2)
entry_assignmentFolder.grid(column=2, row=2)
button_explore1.grid(column = 3, row = 2)

label_submissionsFolder.grid(column=1, row=3)
entry_submissionsFolder.grid(column=2, row=3)
button_explore3.grid(column = 3, row = 3)

button_sortSubmissions.grid(column=4, row=5)

check_rename.grid(column=0, row=5)

# select checkbox so defaults to simplify file names
check_rename.select()

# -----------
window.mainloop()   