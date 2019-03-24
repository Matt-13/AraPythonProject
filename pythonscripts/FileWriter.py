# Code passes the PEP8 check.
import os


class FileWriter:
    def __init__(self):
        pass

    @staticmethod
    def write_file(code, file_name):
        #text_file = open(str(file_name), "w")
        #text_file.write("hello")
        #print(code, file_name)


        with open('Output.txt', 'w') as text_file:
            text_file.write("hello")
            text_file.close()