# Code passes the PEP8 check.

# Ignore errors here.
from FileHandler import FileConverter
from FileView import FileView
from FileWriter import FileWriter
import os

fconv = FileConverter()
fw = FileWriter()
fv = FileView()


class FileController:
    def __init__(self):
        self.command = ''
        self.data = 'empty'
        self.file_location = ''

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
                          "Graph.txt in the root directory!" + str(f))
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
                          "Expected Syntax: lload {filename.txt}")
                else:
                    print("\n==========ERROR==========\n"
                          "File Type Error - File must end in .txt!\n"
                          "Expected Syntax: lload {filename.txt}")

        except SyntaxError as s:
            print("Syntax Error:" + str(s))
        except TabError as t:
            print("Please remove tabs from your command." + str(t))
        except ValueError as v:
            print("Please use the correct command syntax" + str(v))
        except FileNotFoundError as f:
            print("File not found." + str(f))

    # Reads file - Liam
    def read_file(self, filename):
        fconv.read_file(filename)
        fconv.convert_file()
        fconv.return_program()
        self.data = fconv.codeToText
        fw.write_file(self.data, "Output.txt")
        fw.write_file(self.data, "Output.py")

    # Liam
    def print_file(self):
        fv.display_graph_code(self.data)

    # Liam
    def save_file(self, file_name):
        fw.write_file(self.data, file_name)
        print(self.data)

    # Matthew
    def quit(self):
        pass

    # Matthew
    @staticmethod
    def view_help():
        fv.print_help()

    # Matthew
    @staticmethod
    def output(message):
        if message == "e":
            fv.general_error()
        fv.output(message)
