# Made by Matt - does console output related statements.
# Code passes the PEP8 Check.
import os


class FileView:
    # File Handler and FileController Methods
    def __init__(self):
        self.error_message = "\n==========ERROR==========\n"

    def general_error(self):
        print(self.error_message)

    # File Controller Methods
    # Made by Liam and Matt
    @staticmethod
    def print_help():
        # Matt's Code
        print("\n\n")
        print("==================== "
              "Graph Interpreter Help File "
              "====================")
        print("")
        print("NOTE: FileExecuter.py "
              "does not need a command to run")
        print("NOTE: FileExecuter.py "
              "expects a graph.txt in the root directory.")
        print("      if running without a command.")
        print("Command syntax: FileExecuter.py {optionalcommand}")
        print("")
        print("HELP.........................."
              "...........................Displays this help page")
        print("LOAD {filename.txt}......................"
              "...Loads a file from the root directory")
        print("ABSLOAD {path_to_file\\filename.txt}......"
              ".....Loads a file from an absolute path")

        # Liam's Code
        print("LOADCODE {Code_ID}......................."
              "..........Loads code from the data base")
        print("PRINTCODE {Code_ID}................."
              "...Prints code from the data base to the cmd")
        print("SAVE {filename.txt}{Code_ID}..........."
              "..Saves code from database to a text file")
        print("PRINTFILE ................................."
              "...........Prints code from self.data")

    @staticmethod
    def fc_defaults(file_location):
        print("Command not entered. Looking for a "
              "Graph.txt in root directory, "
              "and directory above... ")
        print("Looking in: {} {}"
              .format(os.path.abspath(file_location),
                      "and directory above."))

    @staticmethod
    def fc_file_found():
        print("\nFile Found! Reading..\n")

    @staticmethod
    def fc_file_not_found(file_location, directory, command):
        if directory == "r":
            print("File not found! There must be a "
                  "{}.txt in the root directory!"
                  .format(file_location))
        elif directory == "a":
            print("File not found! There must be a "
                  "{}.txt in the chosen directory!"
                  .format(file_location))
        elif directory == "":
            if command == "load":
                print("No filename entered.\n"
                      "Expected Syntax: load {filename.txt}")
            elif command == "absload":
                print("No filename entered.\n"
                      "Expected Syntax: "
                      "absload {path_to_file\\filename.txt}")

    @staticmethod
    def fc_syntax_error(command):
        if command == "load":
            print("Syntax Error\n"
                  "Expected Syntax: load {filename.txt}")
        elif command == "absload":
            print("File Type Error - File must end in .txt!\n"
                  "Expected Syntax: absload "
                  "{path_to_file\\filename.txt}")

    @staticmethod
    def fc_permission_error():
        print("File permission error! "
              "Make sure you have the "
              "correct read permission on the file")

    @staticmethod
    def fc_load_file_error(file_location):
        print("File not found! '{}'"
              .format(os.path.abspath(file_location)))
    # File Handler Methods
    # File Converter Methods

    @staticmethod
    def fc_plantuml_converting():
        print("Converting file to python syntax..")

    # File Reader Methods
    @staticmethod
    def fr_plantuml_classes_not_found():
        print("Classes not found! Exiting..")

    @staticmethod
    def fr_file_accepted():
        print("File Accepted.. Continuing..")

    @staticmethod
    def file_written(file):
        print("\nFile(s) Successfully Written to Disk: " +
              file)

    @staticmethod
    def fr_plantuml_error():
        print("File not in PlantUML Syntax! "
              "Program Stopping..")

    # File Executer Methods
    @staticmethod
    def fe_defaults():
        print("\nNo arguments entered.. "
              "Continuing with defaults.")

    @staticmethod
    def fe_too_many_args():
        print("\nToo many arguments entered. "
              "Please enter at most 2.")

    @staticmethod
    def fe_command_syntax(name):
        print("{} requires a filename to {} with\n"
              "Syntax: {} [filename.txt]"
              .format(name, str(name).lower(), name))

    @staticmethod
    def fe_loadcode_syntax(text):
        print("{} requires the ID to know which code\n"
              "to load within the database.\n"
              "Syntax: {} [code_id]"
              .format(text, text))

    @staticmethod
    def fe_abs_syntax():
        print("absload requires a file to load.\n"
              "Syntax: absload {path_to_file\\filename.txt}")

    @staticmethod
    def fe_abs_path_error():
        print("Path must be an absolute path.")

    # Other Methods
    @staticmethod
    def output(message):
        print(str(message))

    @staticmethod
    def display_graph_code(code):
        print(code)

    @staticmethod
    def display(data):
        print(data)

    @staticmethod
    def file_error():
        print("")
