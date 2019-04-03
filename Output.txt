# File generated & created on: 2019-04-03 12:14:57.508609
# File passes the PEP8 check.


class FileController:

    command: str

    def __init__(self):
        fileexecuter = FileExecuter()  # association of

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
        filecontroller = FileController()  # composition of

        pass

    def file_validate(self):
        pass


class FileReader:

    file: str
    contents: str

    def __init__(self):
        fileverifier = FileVerifier()  # composition of

        pass

    def add_file(self):
        pass

    def open_file(self):
        pass

    def read_data(self):
        pass


class FileView:

    def __init__(self):
        filecontroller = FileController()  # composition of
        filereader = FileReader()  # aggregation of

        pass

    def display_graph_code(self):
        pass


class FileWriter:

    def __init__(self):
        fileview = FileView()  # aggregation of

        pass

    def write_file(self):
        pass


class FileExecuter:

    def __init__(self):

        pass

    def main(self):
        pass

