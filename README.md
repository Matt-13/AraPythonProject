# AraPythonProject
### Description
Python Project for Ara Sem 1 2019


## This assignment got 89.5/100 please feel free to use as a reference.



## Authors

1. Matthew Whitaker 
    1. Email: _mgw0087@arastudent.ac.nz_
2. Liam Brydon 
    1. Email: _lab0442@arastudent.ac.nz_

## Help & How to

### Command Line Parameters

1. HELP Displays this help page
2. LOAD {filename\filename.txt} Loads a file from the root directory - Will look in the Current Execution Directory (Use CMD CD command to change the directory- otherwise it will look in C:\Windows\System32 or %userprofile%)
3. ABSLOAD {path_to_filename\filename.txt} Loads a file from an absolute path - ABSLOAD Stands for "Absolute Load" from a long absolute path.

4. SAVE {filename.txt} {optional_code_id} Saves code from the DB to a file the user specifies. 
5. LOADCODE {code_id} Saves the code to self.data from the database.
6. PRINTCODE {code_id} Prints code from the database to the console window.

### General Usage

1. Run FileExecuter.py with a python interpreter. (preferably python 3.7 😉) 
2. Make sure modules are installed.
3. For Defaults, make sure the Graph.txt is in the folder with Main.py or FileExecuter.py.
4. Files must be in .txt format.
5. Graph Files must be in the pythonscripts folder (or directory above) - only if the load command/or defaults are used.
6. Graph Files must be in PLANTUML format and begin with @plantuml and end with @enduml
7. Program will not execute from a Network Directory or the root of C:/ Drive.
