""" Made by 3 students:
    Matthew Whitaker
    Liam Brydon
    Sarah Ball (providing the model)
"""
# Code passes the PEP8 Check.

import datetime
from pythonscripts.FileView import FileView
fv = FileView()


class FileConverter:
    def __init__(self):
        self.classes = []
        self.converted_classes = []
        self.codeToText = ""

    # Made by Sarah - Modified by Matt
    def convert_file(self):
        fv.fc_plantuml_converting()
        for class_info in self.classes:
            class_name = class_info.split(' ')[1]
            attributes = []
            methods = []
            for line in class_info.split("\n"):
                if line.find(":") != -1:
                    attributes.append(line)
            for line in class_info.split("\n"):
                if line.find("()") != -1:
                    methods.append(line)
            self.add_class(class_name, attributes, methods)

    # Made by Sarah
    def add_class(self, class_name, attributes, methods):
        new_class = ClassBuilder(class_name, attributes, methods)
        new_class.add_class_attributes()
        new_class.add_class_methods()
        self.converted_classes.append(new_class)

    # Made by Sarah
    def print_program(self):
        for x in self.converted_classes:
            x.print_class()

    # Made by Liam
    # Modified by Matt to pass the PEP8 checks.
    def return_program(self):
        out = "# File generated & created on: " + str(datetime.datetime.now())
        out += "\n# File passes the PEP8 check."
        out += "\n\n"
        for x in self.converted_classes:
            out += (x.return_class())
        self.codeToText += out

    # Made by Matt & Liam
    def read_file(self, file):
        with open(file, "r") as filename:
            data = filename.read()
        rduml = FileReader(data)
        self.classes = rduml.find_classes()


fc = FileConverter()


# Made by Liam & Matt
class FileReader:
    def __init__(self, filename):
        self.allMyClasses = []
        self.code = filename

    # Made by Matt
    def check_if_plantuml(self, code):
        try:
            if code.startswith("@startuml") and code.endswith("@enduml"):
                return True
            else:
                return False
        except Exception as e:
            print(e)

    # Made by Liam
    # Check if the file contains the word "Class"
    def count_occurrences(self, word, sentence):
        try:
            if sentence.lower().split().count(word) > 0:
                return sentence.lower().split().count(word)
            elif sentence.lower().split().count(word) == 0:
                fv.fr_plantuml_classes_not_found()
        except Exception as e:
            print(e)

    # Made by Liam & Matt
    def find_classes(self):
        try:
            isplantuml = self.check_if_plantuml(self.code)
            if isplantuml:
                fv.fr_file_accepted()
                value = self.count_occurrences("class", self.code)
                print(value)

                for i in range(0, value):
                    self.allMyClasses.append(self.code.split("}\nclass")[i])

                return self.allMyClasses
            else:
                fv.fr_plantuml_error()
        except Exception as e:
            print(e)


# Made by Sarah
class ClassBuilder:
    def __init__(self, class_name, new_attributes, new_methods):
        self.name = class_name
        self.attributes = new_attributes
        self.methods = new_methods
        self.all_my_attributes = []
        self.all_my_methods = []

    def add_class_attributes(self):
        for an_attribute in self.attributes:
            new_a_name = an_attribute.split(": ")[0]
            new_a_return = an_attribute.split(": ")[1]
            new_a = Attribute(new_a_name, new_a_return)
            self.all_my_attributes.append(new_a)

    def add_class_methods(self):
        for a_method in self.methods:
            new_m_name = a_method.split(":")[0]
            new_m_return = a_method.split("()")[1]
            new_m = Method(new_m_name, new_m_return)
            self.all_my_methods.append(new_m)

    # Liam Brydon's modified code (originally created by Sarah Ball)
    # Used only for debug!
    def print_class(self):
        print("class", self.name, ":", end="\n\n")
        for x in self.all_my_attributes:
            print(x)
        print("")
        print("\tdef __init__(self):")
        print("\t\tpass")
        for x in self.all_my_methods:
            print(x)
        print("\n")

    # Made by Liam
    def return_class(self):
        out = ""
        out += str("\n")
        out += str("class {}:").format(self.name)
        out += str("\n\n")

        length = len(self.all_my_attributes)
        count = 0
        for x in self.all_my_attributes:
            if count == length - 1:
                out += str("{}".format(x))
                out += str("\n\n")
                count += 1
            elif count < length:
                out += str("{}".format(x))
                out += str("\n")
                count += 1

        out += str("    " + "def __init__(self):\n")
        out += str("        " + "pass\n\n")

        for x in self.all_my_methods:
            out += str("{}".format(x))
            out += str("\n\n")
        return out


"""
Sarah Ball's code - Modified by Liam + Matt
for compatibility with PEP8
"""


class Attribute:
    def __init__(self, new_name, new_return):
        self.name = new_name
        self._return = new_return
        self.name = self.name.strip(' ')

    def __str__(self):
        if self._return == "String":
            return f"    {self.name}: str "
        elif self._return == "Integer":
            return f"    {self.name}: int "
        elif self._return == "ArrayObject":
            return f"    {self.name}: list "
        elif self._return == "Object":
            return f"    {self.name}: object "
        else:
            return f"    {self.name}: '{self._return}' "


"""
Sarah Ball's code - Modified by Liam + Matt
for compatibility with PEP8
"""


class Method:
    def __init__(self, new_name, new_return):
        self.name = new_name.replace("()", "")
        self._return = new_return

    def __str__(self):
        return f"    def {self.name}(self):\n        pass"
