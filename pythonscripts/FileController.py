# Code passes the PEP8 check.

# Ignore errors here.
from pythonscripts.FileHandler import FileConverter
from pythonscripts.FileView import FileView
from pythonscripts.FileWriter import  FileWriter
import os
from pythonscripts.DataBase import *

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
                fv.fc_defaults(file_location)
                try:
                    if os.path.isfile("../Graph.txt"):
                        fv.fc_file_found()
                        self.read_file("../Graph.txt")
                    elif os.path.isfile("./Graph.txt"):
                        fv.fc_file_found()
                        self.read_file("./Graph.txt")
                    else:
                        fv.general_error()
                        fv.fc_file_not_found(file_location, "r")
                except Exception as e:
                    pass
            elif self.command == "load":
                if file_location.endswith(".txt"):
                    try:
                        if os.path.isfile("../{}".format(file_location)):
                            fv.fc_file_found()
                            self.read_file("../{}".format(file_location))
                        elif os.path.isfile("./{}".format(file_location)):
                            fv.fc_file_found()
                            self.read_file("./{}".format(file_location))
                        else:
                            fv.general_error()
                            fv.fc_load_file_error(file_location)
                    except FileNotFoundError:
                        fv.fc_file_not_found(file_location, "r", "load")
                    except PermissionError:
                        fv.fc_permission_error()
                elif file_location == "":
                    fv.general_error()
                    fv.fc_file_not_found(file_location, "", "load")
                else:
                    fv.general_error()
                    fv.fc_syntax_error("load")
            elif self.command == "absload":
                if file_location.endswith(".txt"):
                    try:
                        if os.path.isfile("{}".format(file_location)):
                            fv.fc_file_found()
                            self.read_file("../{}".format(file_location))
                        else:
                            fv.general_error()
                            fv.fc_load_file_error(file_location)
                    except FileNotFoundError:
                        fv.fc_file_not_found(file_location, "a", "absload")
                    except PermissionError:
                        fv.fc_permission_error()
                elif file_location == "":
                    fv.general_error()
                    fv.fc_file_not_found(file_location, "", "absload")
                else:
                    fv.general_error()
                    fv.fc_syntax_error("absload")
        except FileNotFoundError:
            fv.fc_load_file_error(file_location)

    # Reads file - Liam
    def read_file(self, filename):
        fconv.read_file(filename)
        fconv.convert_file()
        fconv.return_program()
        self.data = fconv.codeToText
        fw.write_file(self.data, "Output.txt")
        fw.write_file(self.data, "Output.py")
        create_table()
        data_entry(self.data)
        #fv.file_written("Output.txt, Output.py")

    # Liam
    def print_file(self):
        fv.display_graph_code(self.data)

    # Liam
    def save_file(self, file_name):
        self.data = get_code(5)
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
