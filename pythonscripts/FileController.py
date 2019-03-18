from FileHandler import FileConverter
from FileView import FileView
import os

fcon = FileConverter()
fv = FileView()

class FileController:
    def __init__(self):
        self.command = ''
        self.data = ''
        self.file_location = ''

    def display(self):
        pass

    # Command Handler - Made by Matthew
    def handle_command(self, cmd, file_location):
        self.file_location = file_location
        self.command = cmd
        try:
            if self.command == "":
                print("Command not entered. Looking for a Graph.txt in root directory, and directory above... ")
                print("Looking in: {} {}".format(os.path.abspath(file_location), "and directory above."))
                try:
                    if os.path.isfile("../Graph.txt"):
                        print("\nFile Found! Reading..\n")
                        self.read_file("../Graph.txt")
                    elif os.path.isfile("./Graph.txt"):
                        print("\nFile Found! Reading..\n")
                        self.read_file("./Graph.txt")
                except FileNotFoundError as f:
                    print("File not found! There must be a Graph.txt in the root directory!" + f)
            elif self.command == "load":
                if file_location.endswith(".txt"):
                    try:
                        if os.path.isfile("../{}".format(file_location)):
                            print("\nFile Found! Reading..\n")
                            self.read_file("../{}".format(file_location))
                        elif os.path.isfile("./{}".format(file_location)):
                            print("\nFile Found! Reading..\n")
                            self.read_file("./{}".format(file_location))
                        else:
                            print("\n==========ERROR==========\nFile not found! '{}'"
                                  .format(os.path.abspath(file_location)))
                    except FileNotFoundError as f:
                        print("File not found! There must be a {}.txt "
                              "in the root directory! {}".format(file_location, f))
                elif file_location == "":
                    print("No filename entered.\nExpected Syntax: load {filename.txt}")
                else:
                    print("\n==========ERROR==========\nSyntax Error\nExpected Syntax: load {filename.txt}")
            elif self.command == "lload":
                self.read_file(file_location)

        except SyntaxError as s:
            print("Syntax Error:" + s)
        except TabError as t:
            print("Please remove tabs from your command." + t)
        except ValueError as v:
            print("Please use the correct command syntax" + v)
        except FileNotFoundError as f:
            print("File not found." + f)

    # Reads file - Liam
    def read_file(self, filename):
        self.data = fcon.read_file(filename)

    # Not sure if needed! - Matthew
    def quit(self):
        pass

    def view_help(self):
        print("\n\n")
        print("==================== Graph Interpreter Help File ====================")
        print("")
        print("NOTE: FileExecuter.py does not need a command to run")
        print("NOTE: FileExecuter.py expects a graph.txt in the root directory.")
        print("Command syntax: FileExecuter.py {optionalcommand}")
        print("")
        print("HELP..........................................Displays this help page")
        print("LOAD {filename}..................Loads a file from the root directory")
        print("LLOAD {path_to_filename}...........Loads a file from an absolute path")

