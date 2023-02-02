* Please place the folder with this source code in the same directory as your course folders

# folderGenerator.py ------------------------------------
This is a simple Python script that lets you quickly generate folders for each assignment, as well as folders for each student in each assignment. 
The script will ask for the name of the class folder, the assignment type (Lab, Project, etc), and the number of that assignment. 
It will then create a folder for each of those assignments (ex. Lab3)
Inside each of those assignment folders, it will create a folder for each student.

Later, you can use sortSubmissions.py to sort all submissions into each student's folder. 


## How to Run:
    1. Make sure to have a "classlist.csv" file in the class director with student's last name, first name
        Ex. Mau Justin  
    2. Run with "python3 *folderGenerator.py*
    3. Follow the instructions on the console


# sortSubmissions.py -----------------------------------
This program can help you download all submissions from D2L and separate them neatly into each student's folder.
It will also automatically extract any .zip files in the submissions.

### Why use this program? -
    D2L allows you to download all user submission at once as a large zip file. 
    However, all the files for each student get lumped together in that zip file, with nothing separating user submissions.
    The way D2L names the files doesn't allow you to sort by user either. 
    Also, if some users submit zip files and others submit individual files, the whole thing becomes a mess to sort through. 
    This program allows you to neatly organize all student submissions, as well as unpack all the zip files included.

## How to Run:
    1. Make sure to have a "classlist.csv" file in the class directory with student's last name, first name
        Ex. Mau Justin  
    2. Download all submissions from D2L (.zip)
    3. Extract that zip to a folder named "_submissions" in that assignment's directory
    4. Run with "python3 sortSubmissions.py"
    5. Follow the instructions on the console
    6. All files associated with each student's submission should now be in that student's respective folder