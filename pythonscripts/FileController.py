from FileHandler import FileVerifier
from FileView import FileView


class FileController:
    def __init__(self):
        self.command = ''

    def display(self):
        pass

    def handle_command(self, cmd):
        self.command = cmd
        try:
            if cmd == "":
                print("Command not entered. Continuing... ")
                # Go to conversion + file reader
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
