# File generated & created on: 2019-04-03 20:36:12.384983
# File passes the PEP8 check.


class FileController:

    command: str

    def __init__(self):
        self.fileexecuter = FileExecuter()  # association of

        pass

    def display(self):
        pass

    def handle_command(self):
        pass

    def read_file(self):
        pass

    def quit(self):
        pass

    def validate(self):
        pass

    def view_help(self):
        pass


class FileVerifier:

    theData: str

    def __init__(self):
        self.filecontroller = FileController()  # composition of

        pass

    def file_validate(self):
        pass


class FileReader:

    file: str
    contents: str

    def __init__(self):
        self.fileverifier = FileVerifier()  # composition of

        pass

    def add_file(self):
        pass

    def open_file(self):
        pass

    def read_data(self):
        pass


class FileView:

    def __init__(self):
        self.filecontroller = FileController()  # composition of
        self.filereader = FileReader()  # aggregation of

        pass

    def display_graph_code(self):
        pass


class FileWriter:

    def __init__(self):
        self.fileview = FileView()  # aggregation of

        pass

    def write_file(self):
        pass


class FileExecuter:

    def __init__(self):

        pass

    def main(self):
        pass

# File generated & created on: 2019-04-03 20:36:14.280750
# File passes the PEP8 check.


class FileController:

    command: str

    def __init__(self):
        self.fileexecuter = FileExecuter()  # association of

        pass

    def display(self):
        pass

    def handle_command(self):
        pass

    def read_file(self):
        pass

    def quit(self):
        pass

    def validate(self):
        pass

    def view_help(self):
        pass


class FileVerifier:

    theData: str

    def __init__(self):
        self.filecontroller = FileController()  # composition of

        pass

    def file_validate(self):
        pass


class FileReader:

    file: str
    contents: str

    def __init__(self):
        self.fileverifier = FileVerifier()  # composition of

        pass

    def add_file(self):
        pass

    def open_file(self):
        pass

    def read_data(self):
        pass


class FileView:

    def __init__(self):
        self.filecontroller = FileController()  # composition of
        self.filereader = FileReader()  # aggregation of

        pass

    def display_graph_code(self):
        pass


class FileWriter:

    def __init__(self):
        self.fileview = FileView()  # aggregation of

        pass

    def write_file(self):
        pass


class FileExecuter:

    def __init__(self):

        pass

    def main(self):
        pass


class FileController:

    command: str

    def __init__(self):
        self.fileexecuter = FileExecuter()  # association of

        pass

    def display(self):
        pass

    def handle_command(self):
        pass

    def read_file(self):
        pass

    def quit(self):
        pass

    def validate(self):
        pass

    def view_help(self):
        pass


class FileVerifier:

    theData: str

    def __init__(self):
        self.filecontroller = FileController()  # composition of

        pass

    def file_validate(self):
        pass


class FileReader:

    file: str
    contents: str

    def __init__(self):
        self.fileverifier = FileVerifier()  # composition of

        pass

    def add_file(self):
        pass

    def open_file(self):
        pass

    def read_data(self):
        pass


class FileView:

    def __init__(self):
        self.filecontroller = FileController()  # composition of
        self.filereader = FileReader()  # aggregation of

        pass

    def display_graph_code(self):
        pass


class FileWriter:

    def __init__(self):
        self.fileview = FileView()  # aggregation of

        pass

    def write_file(self):
        pass


class FileExecuter:

    def __init__(self):

        pass

    def main(self):
        pass

