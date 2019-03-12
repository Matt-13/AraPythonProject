# Import modules here
# from plantuml import *
import os
import sys

# sys.argv[2] - import command line args.


# FileReader Example
class ReadPlantUML:
    def __init__(self, filename):
        self.allMyClasses = []
        self.code = filename

    # Check if the file contains the word "Class"
    def count_occurrences(self, word, sentence):
        try:
            if sentence.lower().split().count(word) > 0:
                return sentence.lower().split().count(word)
            elif sentence.lower().split().count(word) == 0:
                print("Word not found.")
        except Exception as e:
            print(e)

    def find_classes(self):
        value = self.count_occurrences("class", self.code)

        for i in range(0, value):
            self.allMyClasses.append(self.code.split("class")[i + 1])

        return self.allMyClasses


class ClassConverter:
    def __init__(self, class_string):
        self.class_string = class_string
        self.class_name = ''
        self.allMyClassAttributes = []
        self.allMyClassMethods = []

    def find_methods(self):
        pass

    def find_attributes(self):
        pass


# FileVerifier Example
class ConvertPlantUML:
    def __init__(self):
        self.classes = []

    def check_file(self):
        print("Checking file..")
        # For string(class) in self.stringClasses
        #     classobject = ClassConverter(class)
        #     self.objectClasses.append(classobject)

    def read_file(self, file):
        with open(file, "r") as filename:
            data = filename.read().replace('\n', ' ')
        rduml = ReadPlantUML(data)
        self.classes = rduml.find_classes()


rd = ConvertPlantUML()
rd.read_file("Graph.txt")
print(rd.classes)
rd.check_file()

"""
contents = Alice -> Bob: test
if os.path.exists("Graph.txt"):
    os.remove("Graph.txt")
if os.path.exists("Graph.png"):
    os.remove("Graph.png")
else:
    print("The file does not exist. skipping...")
file = open("Graph.txt", "x")
file.write("@startuml\n")
file.write(contents + "\n")
file.write("@enduml")
"""

# Refresh Graph
# os.system('C:\\Windows\\System32\\cmd.exe /c CreateGraph.bat')
