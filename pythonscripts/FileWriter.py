class FileWriter:
    def __init__(self):
       pass

    @staticmethod
    def write_file(code):
        text_file = open("Output.txt", "w")
        text_file.write(str(code))
        text_file.close()
