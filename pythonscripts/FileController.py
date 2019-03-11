from FileHandler import FileVerifier
from FileView import FileView


class FileController:
    def __init__(self):
        self.species = 'Human'
        self.command = ''

    def display(self):
        pass

    def handlecommand(self, cmd):
        self.command = cmd
        print(self.command)

    def readfile(self):
        pass

    def quit(self):
        pass

    def validate(self):
        pass

    def viewhelp(self):
        pass

    @classmethod
    def get_species(cls):
        return cls.species
