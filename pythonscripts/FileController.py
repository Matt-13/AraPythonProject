from FileHandler import FileConverter
from FileView import FileView

fcon = FileConverter()
fv = FileView()

class FileController:
    def __init__(self):
        self.command = ''

    def display(self):
        pass

    def handle_command(self, cmd):
        self.command = cmd
        try:
            if cmd == "":
                print("Command not entered. Continuing with default Graph.txt in root directory... ")
            if cmd == "--help":
                print("Displaying help file.")
            if cmd == "--load":
                print("Loading file..")
        except SyntaxError as s:
            print("Syntax Error:" + s)
        except TabError as t:
            print("Please remove tabs from your command." + t)
        except ValueError as v:
            print("Please use the correct command syntax" + v)
        print(self.command)

    def read_file(self):
        pass

    def quit(self):
        pass

    def validate(self):
        pass

    def view_help(self):
        pass

    @classmethod
    def get_species(cls):
        return cls.species
