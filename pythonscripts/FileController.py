from FileHandler import FileConverter
from FileView import FileView
from FileWriter import FileWriter
import os

fcon = FileConverter()
fw = FileWriter()
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
                print("Command not entered. Looking for a "
                      "Graph.txt in root directory, "
                      "and directory above... ")
                print("Looking in: {} {}"
                      .format(os.path.abspath(file_location),
                              "and directory above."))
                try:
                    if os.path.isfile("../Graph.txt"):
                        print("\nFile Found! Reading..\n")
                        self.read_file("../Graph.txt")
                    elif os.path.isfile("./Graph.txt"):
                        print("\nFile Found! Reading..\n")
                        self.read_file("./Graph.txt")
                except FileNotFoundError as f:
                    print("File not found! There must be a "
                          "Graph.txt in the root directory!" + f)
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
                            print("\n==========ERROR==========\n"
                                  "File not found! '{}'"
                                  .format(os.path.abspath(file_location)))
                    except FileNotFoundError as f:
                        print("File not found! There must be a {}.txt "
                              "in the root directory! {}"
                              .format(file_location, f))
                    except PermissionError as p:
                        print("File permission error! "
                              "Make sure you have the "
                              "correct read permission on the file"
                              "{}".format(p))
                elif file_location == "":
                    print("No filename entered.\n"
                          "Expected Syntax: load {filename.txt}")
                else:
                    print("\n==========ERROR==========\n"
                          "Syntax Error\n"
                          "Expected Syntax: load {filename.txt}")
            elif self.command == "lload":
                if file_location.endswith(".txt"):
                    try:
                        if os.path.isfile("{}".format(file_location)):
                            print("\nFile Found! Reading..\n")
                            self.read_file("../{}".format(file_location))
                        else:
                            print("\n==========ERROR==========\n"
                                  "File not found! '{}'"
                                  .format(os.path.abspath(file_location)))
                    except FileNotFoundError as f:
                        print("File not found! "
                              "Please check your absolute path. "
                              "{}".format(file_location, f))
                    except PermissionError as p:
                        print("File permission error! "
                              "Make sure you have the "
                              "correct read permission on the file"
                              "{}".format(p))
                elif file_location == "":
                    print("No filename entered.\n"
                          "Expected Syntax: load {filename.txt}")
                else:
                    print("\n==========ERROR==========\n"
                          "Syntax Error\n"
                          "Expected Syntax: load {filename.txt}")

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
        fcon.read_file(filename)
        # @Liam - you missed this ;)
        fcon.convert_file()
        fcon.return_program()

        # need to fix below here now. - somewhere in the filehandler it isn't sending back.
        self.data = fcon.codeToText
        print(self.data)
        fw.write_file(self.data, "Output.txt")

    # Not sure if needed! - Matthew
    def quit(self):
        pass

    def view_help(self):
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
              "................Displays this help page")
        print("LOAD {filename}..............."
              "...Loads a file from the root directory")
        print("LLOAD {path_to_filename}......"
              ".....Loads a file from an absolute path")
