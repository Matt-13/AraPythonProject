# Made by Matt - does console output related statements.
# Code passes the PEP8 Check.


class FileView:
    def __init__(self):
        self.error_message = "==========ERROR=========="

    def general_error(self):
        print(self.error_message)

    @staticmethod
    def plantuml_error():
        print("File not in PlantUML Syntax! Program Stopping..")

    @staticmethod
    def plantuml_converting():
        print("Converting file to python syntax..")

    @staticmethod
    def plantuml_classes_not_found():
        print("Classes not found! Exiting..")

    @staticmethod
    def file_error():
        print("")

    @staticmethod
    def file_accepted():
        print("File Accepted.. Continuing..")

    @staticmethod
    def print_help():
        print("\n\n")
        print("==================== "
              "Graph Interpreter Help File "
              "====================")
        print("")
        print("NOTE: FileExecuter.py "
              "does not need a command to run")
        print("NOTE: FileExecuter.py "
              "expects a graph.txt in the root directory.")
        print("      if running without a command.")
        print("Command syntax: FileExecuter.py {optionalcommand}")
        print("")
        print("HELP.........................."
              "................Displays this help page")
        print("LOAD {filename}..............."
              "...Loads a file from the root directory")
        print("LLOAD {path_to_filename}......"
              ".....Loads a file from an absolute path")

    @staticmethod
    def output(message):
        print(str(message))

    @staticmethod
    def display_graph_code(code):
        print(code)
