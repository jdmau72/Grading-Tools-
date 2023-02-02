# Program: sortSubmissions.py
# Author: Justin Mau
# Date: 2/2/2023

# --------------
import os
import csv
import shutil
from zipfile import ZipFile


# Main --------------------------------------------------------------------
def main():
    os.chdir(os.getcwd() + "/../")
    print(os.getcwd())

    className = input("Please enter the name of the folder for the class: ")
    os.chdir(os.getcwd() + "/" + className)

    # reads in the classlist
    classlist = []
    with open('classlist.csv', mode = 'r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            classlist.append((line[0] + line[1]).strip(" "))
            
    # gets the directories for assignment folder and submissions 
    assignment = input("What is the name of the assignment folder?: ")
    assignmentDir = os.getcwd() + "/" + assignment
    submissionsDir = assignmentDir + "/_submissions"
    os.chdir(submissionsDir)

    # get all of the files in the submissions folder
    fileList = os.listdir(os.getcwd())
    

    # goes through each student, and find's all the files they submitted
    for student in classlist:
        # sets source and destination for moving files
        source = os.getcwd()
        destination = assignmentDir + f"/{student}"
        
        print(f"{student}'s Submission Contents:")
        for file in fileList:
            if (file.find(student) != -1):

                # moves the file from 
                src_path = os.path.join(source, file)
                dst_path = os.path.join(destination, file)
                shutil.move(src_path, dst_path)
                
                print(file)
                
                # now extracts it if its a zip
                if(file.endswith(".zip")):
                    zip = ZipFile(dst_path)
                    zip.extractall(destination)
                    zip.close()
                    os.remove(dst_path) # removes that zip file 
        print("-----------------------------------")
# end of main() ---------------------------------------------------



if __name__ == "__main__":
    main()