# Code passes the PEP8 check.

# Ignore errors here.
from pythonscripts.FileHandler import FileConverter
from pythonscripts.FileView import FileView
from pythonscripts.FileWriter import  FileWriter
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
                fv.defaults(file_location)
                try:
                    if os.path.isfile("../Graph.txt"):
                        fv.file_found()
                        self.read_file("../Graph.txt")
                    elif os.path.isfile("./Graph.txt"):
                        fv.file_found()
                        self.read_file("./Graph.txt")
                    else:
                        fv.general_error()
                        fv.file_not_found(file_location)
                except Exception as e:
                    pass
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
            elif self.command == "absload":
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
                          "Expected Syntax: absload {path_to_file\\filename.txt}")
                else:
                    print("\n==========ERROR==========\n"
                          "File Type Error - File must end in .txt!\n"
                          "Expected Syntax: absload {path_to_file\\filename.txt}")

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
        fv.file_written("Output.txt, Output.py")

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
    def output_error(message):
        fv.general_error()
        fv.output(message)
