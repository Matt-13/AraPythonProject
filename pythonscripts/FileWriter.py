class FileWriter:
    def __init__(self):
       pass

    @staticmethod
    def write_file(code, file_name):
        text_file = open(str(file_name), "w")
        text_file.write(str(code))
        text_file.close()
