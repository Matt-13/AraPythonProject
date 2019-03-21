# Ignore errors below this line.
import sys
from FileController import FileController


# Execute code here
# Matthew Whitaker's code.
def main(argv):
    fc = FileController()
    # For Debugging Sys.Argv
    # print('Number of arguments:', len(sys.argv), 'arguments.')
    # print('Argument List:', str(sys.argv))
    inputfile = ''
    try:
        if len(sys.argv) < 2:
            print("\nNo arguments entered.. "
                  "Continuing with defaults.")
            fc.handle_command('', '')
        if len(sys.argv) > 3:
            print("\nToo many arguments entered. "
                  "Please enter at most 2.")
        else:
            if str(sys.argv[1]) == "help":
                fc.view_help()
            elif str(sys.argv[1]) == "load":
                if len(sys.argv) == 2:
                    print("\n=======ERROR=======\n"
                          "Load requires a file to load.\n"
                          "Syntax: load {file.txt}")
                else:
                    fc.handle_command("load", str(sys.argv[2]))
            elif str(sys.argv[1] == "lload"):
                if len(sys.argv) == 2:
                    print("\n=======ERROR=======\n"
                          "Lload requires a file to load.\n"
                          "Syntax: lload {path_to_file.txt}")
                if "\\" in str(sys.argv[2]):
                    fc.handle_command("lload", str(sys.argv[2]))
                else:
                    print("Path must be an absolute path.")
    except IndexError as i:
        pass
    except Exception as e:
        pass


def print_to_screen(yesno):
    # if yesno == "y" or yesno == "yes":
    pass


if __name__ == "__main__":
    main(sys.argv[1:])
# print(fc.get_species())
