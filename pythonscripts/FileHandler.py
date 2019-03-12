class FileVerifier:
    def __init__(self):
        self.theData = self

    def file_validate(self):
        pass


fv = FileVerifier()


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
        fv.file_validate(self.contents)
