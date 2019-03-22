# Made by Matt - does console output related statements.
class FileView:
    def __init__(self):
        pass

    def general_error(self):
        print("==========ERROR==========")

    def plantuml_error(self):
        print("File not in PlantUML Syntax! Program Stopping..")

    def plantuml_classes_not_found(self):
        print("Classes not found! Exiting..")

    def file_error(self):
        print("")

    def file_accepted(self):
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
