# Program: folderGenerator.py
# Author: Justin Mau
# Date: 2/2/2023

# --------------
import os
import csv


# Main --------------------------------------------------------------------
def main():
    os.chdir(os.getcwd() + "/../")
    print(os.getcwd())

    className = input("Please enter the name of the folder for the class: ")
    os.chdir(os.getcwd() + "/" + className)
    print(os.getcwd())

    # reads in the classlist
    classlist = []
    with open('classlist.csv', mode = 'r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            classlist.append((line[0] + line[1]).strip(" "))

    # gets either Lab, Project, Assignment
    assignmentType = input("Please enter the assignment type: ")

    # get the number of those assignments
    numAssignments = input("How many of these assignments?: ")


    for i in range(int(numAssignments)):
        # creates a directory assignment
        os.mkdir(assignmentType + str(i + 1))   
        # changes directory to that new folder
        os.chdir(os.getcwd() + f"/{assignmentType}{str(i + 1)}")
        
        # goes through the classlist and creates a folder for each student
        for student in classlist:
            os.mkdir(student)
                
        os.chdir(os.getcwd() + "/../")
        
    print("All done!")
# End of main() ----------------------------------



if __name__ == "__main__":
    main()              
