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

    def handle_command(self, cmd, file_location):
        self.command = cmd
        self.file_location = file_location
        try:
            if cmd == "":
                print("Command not entered. Looking for a Graph.txt in root directory, and directory above... ")
                try:
                    if os.path.isfile("../Graph.txt"):
                        self.read_file("../Graph.txt")
                    elif os.path.isfile("./Graph.txt"):
                        self.read_file("./Graph.txt")
                except FileNotFoundError as f:
                    print("File not found! There must be a Graph.txt in the root directory!" + f)
            if cmd == "load":
                if file_location.endswith(".txt"):
                    try:
                        if os.path.isfile("../{}").format(file_location):
                            self.read_file("../{}").format(file_location)
                        elif os.path.isfile("./{}").format(file_location):
                            self.read_file("./{}").format(file_location)
                    except FileNotFoundError as f:
                        print("File not found! There must be a {}.txt in the root directory!" + f).format(file_location)
                elif not file_location.endswith(".txt"):
                    try:
                        if os.path.isfile("../{}.txt").format(file_location):
                            self.read_file("../{}.txt").format(file_location)
                        elif os.path.isfile("./{}.txt").format(file_location):
                            self.read_file("./{}.txt").format(file_location)
                    except FileNotFoundError as f:
                        print("File not found! There must be a {}.txt in the root directory!" + f).format(file_location)
                print("Loading file in root directory..")
            if cmd == "lload":
                self.read_file(file_location)

        except SyntaxError as s:
            print("Syntax Error:" + s)
        except TabError as t:
            print("Please remove tabs from your command." + t)
        except ValueError as v:
            print("Please use the correct command syntax" + v)
        except FileNotFoundError as f:
            print("File not found." + f)
        print(self.command)

    def read_file(self, filename):
        self.data = fcon.read_file(filename)
        print(self.data)

    def quit(self):
        pass

    def view_help(self):
        print("\n\n")
        print("==================== Graph Interpreter Help File ====================")
        print("")
        print("FileExecuter.py does not need a command to run")
        print("Command syntax: FileExecuter.py {optionalcommand}")
        print("")
        print("HELP..........................................Displays this help page")
        print("LOAD {filename}..................Loads a file from the root directory")
        print("LLOAD {path_to_filename}...........Loads a file from an absolute path")

