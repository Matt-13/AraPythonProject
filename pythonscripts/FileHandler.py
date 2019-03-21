class FileConverter:
    def __init__(self):
        self.classes = []
        self.converted_classes =[]
        self.codeToText = ""

    def convert_file(self):
        print("Converting file to python syntax..")
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

    def add_class(self, class_name, attributes, methods):
        new_class = ClassBuilder(class_name, attributes, methods)
        new_class.add_class_attributes()
        new_class.add_class_methods()
        self.converted_classes.append(new_class)

    def print_program(self):
        for x in self.converted_classes:
            x.print_class()

    def return_program(self):
        out = ""
        for x in self.converted_classes:
            out += (x.return_class())
        self.codeToText += out

    def read_file(self, file):
        with open(file, "r") as filename:
            data = filename.read()
        rduml = FileReader(data)
        self.classes = rduml.find_classes()
        self.return_program()


fc = FileConverter()


class FileReader:
    def __init__(self, filename):
        self.allMyClasses = []
        self.code = filename

    def check_if_plantuml(self, code):
        try:
            if code.startswith("@startuml") and code.endswith("@enduml"):
                return True
            else:
                return False
        except Exception as e:
            print(e)

    # Check if the file contains the word "Class"
    def count_occurrences(self, word, sentence):
        try:
            if sentence.lower().split().count(word) > 0:
                return sentence.lower().split().count(word)
            elif sentence.lower().split().count(word) == 0:
                print("Classes not found.")
        except Exception as e:
            print(e)

    def find_classes(self):
        try:
            isplantuml = self.check_if_plantuml(self.code)
            if isplantuml:
                print("File Accepted! Continuing..")
                value = self.count_occurrences("class", self.code)

                for i in range(0, value):
                    self.allMyClasses.append(self.code.split("class")[i + 1])

                return self.allMyClasses
            else:
                print("Program Stopping..")
        except Exception as e:
            print(e)



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

    def return_class(self):
        out = ""
        out += str("class {}:").format(self.name)
        out += str("\n\n")

        for x in self.all_my_attributes:
            out += str("\n {}".format(x))
        out += str("")
        out += str("\t" + "def __init__(self):")
        out += str("\t\t" + "pass")
        for x in self.all_my_methods:
            out += str(x)
        out += str("\n")
        return out


# Sarah Ball's code - Modified by Liam + Matt for compatibility with tab escape characters.
class Attribute:
    def __init__(self, new_name, new_return):
        self.name = new_name
        self._return = new_return

    def __str__(self):
        return f"\t{self.name}= {self._return}"


# Sarah Ball's code - Modified by Liam + Matt for compatibility with tab escape characters.
class Method:
    def __init__(self, new_name, new_return):
        self.name = new_name.replace("()", "")
        self._return = new_return

    def __str__(self):
        return f"\t{self.name}(self):\n\t\tpass"
