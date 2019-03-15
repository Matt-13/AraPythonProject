class FileConverter:
    def __init__(self):
        self.classes = []
        self.convertedclasses = []

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
        self.convertedclasses.append(new_class)

    def print_program(self):
        for x in self.convertedclasses:
            x.print_class()

    def read_file(self, file):
        with open(file, "r") as filename:
            data = filename.read().replace('\n', ' ')
        rduml = ReadPlantUML(data)
        self.classes = rduml.find_classes()


fc = FileConverter()


class FileReader:
    def __init__(self):
        self.file = self
        self.contents = ""

    def add_file(self, file_name):
        self.file = file_name

    def open_file(self):
        try:
            with open(self.file, "r") as file:
                self.contents = file.read()
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print("Error: {}".format(e))

    def read_data(self):
        fc.file_validate(self.contents)


fr = FileReader()

