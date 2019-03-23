# Made by Matt - does console output related statements.
# Code passes the PEP8 Check.
import os


class FileView:
    def __init__(self):
        self.error_message = "\n==========ERROR=========="

    def general_error(self):
        print(self.error_message)

    @staticmethod
    def defaults(file_location):
        print("Command not entered. Looking for a "
              "Graph.txt in root directory, "
              "and directory above... ")
        print("Looking in: {} {}"
              .format(os.path.abspath(file_location),
                      "and directory above."))

    @staticmethod
    def file_found():
        print("\nFile Found! Reading..\n")

    @staticmethod
    def file_not_found(f):
        print("File not found! There must be a "
              "Graph.txt in the root directory!" + str(f))

    @staticmethod
    def plantuml_error():
        print("File not in PlantUML Syntax! Program Stopping..")

    @staticmethod
    def plantuml_converting():
        print("Converting file to python syntax..")

    @staticmethod
    def plantuml_classes_not_found():
        print("Classes not found! Exiting..")

    @staticmethod
    def file_error():
        print("")

    @staticmethod
    def file_accepted():
        print("File Accepted.. Continuing..")

    @staticmethod
    def print_help():
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

    @staticmethod
    def file_written(file):
        print("\nFile(s) Successfully Written to Disk: " + file)

    @staticmethod
    def output(message):
        print(str(message))

    @staticmethod
    def display_graph_code(code):
        print(code)
