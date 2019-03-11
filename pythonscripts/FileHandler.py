from FileVerifier import FileVerifier
from FileHandler import *

class FileVerifier:
    def __init__(self):
        self.theData = self

    def filevalidate(self):
        pass

fv = FileVerifier()


class FileReader:
    def __init__(self):
        self.file = self
        self.contents = ""

    def addfile(self, file_name):
        self.file = file_name

    def openfile(self):
        try:
            with open(self.file, "r") as file:
                self.contents = file.read()
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print("Error: {}".format(e))

    def readdata(self):
        fv.filevalidate(self.contents)