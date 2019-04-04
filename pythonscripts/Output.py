# File generated & created on: 2019-04-04 17:33:36.232231
# File passes the PEP8 check.


class FileController:

    command: str
    data: str
    file_location: str

    def __init__(self):
        self.fileexecuter = FileExecuter()  # association of

        pass

    def display(self):
        pass

    def handle_command(self):
        pass

    def read_file(self):
        pass

    def print_file(self):
        pass

    def save_file(self):
        pass

    def quit(self):
        pass

    def view_help(self):
        pass

    def output_error(self):
        pass


class FileConverter:

    classes: list
    converted_classes: list
    codeToText: str

    def __init__(self):
        self.filecontroller = FileController()  # composition of

        pass

    def convert_file(self):
        pass

    def add_class(self):
        pass

    def print_program(self):
        pass

    def return_program(self):
        pass

    def read_file(self):
        pass


class FileReader:

    allMyClasses: list
    code: str

    def __init__(self):
        self.fileconverter = FileConverter()  # composition of

        pass

    def check_if_plantuml(self):
        pass

    def count_occurences(self):
        pass

    def find_classes(self):
        pass


class ClassBuilder:

    name: object
    attributes: object
    methods: object
    all_my_attributes: list
    all_my_methods: list

    def __init__(self):
        self.fileconverter = FileConverter()  # composition of

        pass

    def add_class_attributes(self):
        pass

    def add_class_methods(self):
        pass

    def print_class(self):
        pass

    def return_class(self):
        pass


class Attribute:

    def __init__(self):
        self.classbuilder = ClassBuilder()  # composition of

        pass

    def __str__(self):
        pass


class Method:

    def __init__(self):
        self.classbuilder = ClassBuilder()  # composition of

        pass

    def __str__(self):
        pass


class FileView:

    error_message: str

    def __init__(self):
        self.filecontroller = FileController()  # composition of
        self.filereader = FileReader()  # aggregation of

        pass

    def fc_defaults(self):
        pass

    def fc_file_found(self):
        pass

    def fc_file_not_found(self):
        pass

    def fc_syntax_error(self):
        pass

    def fc_permission_error(self):
        pass

    def fc_load_file_error(self):
        pass

    def fc_plantuml_converting(self):
        pass

    def fc_plantuml_classes_not_found(self):
        pass

    def fr_file_accepted(self):
        pass

    def fr_plantuml_error(self):
        pass

    def file_written(self):
        pass

    def fe_defaults(self):
        pass

    def fe_too_many_args(self):
        pass

    def fe_command_syntax(self):
        pass

    def fe_abs_syntax(self):
        pass

    def fe_abs_path_error(self):
        pass

    def output(self):
        pass

    def general_error(self):
        pass

    def print_help(self):
        pass

    def display_graph_code(self):
        pass

    def file_error(self):
        pass


class FileWriter:

    def __init__(self):
        self.filecontroller = FileController()  # aggregation of

        pass

    def write_file(self):
        pass


class FileExecuter:

    command: str

    def __init__(self):

        pass

    def main(self):
        pass

    def print_to_screen(self):
        pass

