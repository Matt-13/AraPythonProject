# Ignore errors below this line.
import sys
from FileController import FileController


# Execute code here
# Matthew Whitaker's code.
def main(argv):
    fc = FileController()
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    inputfile = ''
    try:
        if len(sys.argv) < 2:
            print("No arguments entered.. Continuing with defaults.")
            fc.handle_command('', '')
        if len(sys.argv) > 3:
            print("Too many arguments entered. Please enter at most 2.")
        else:
            if str(sys.argv[1]) == "help":
                fc.view_help()
            if str(sys.argv[1]) == "load":
                fc.handle_command("load", str(sys.argv[2]))
            if str(sys.argv[1] == "lload"):
                fc.handle_command("lload", str(sys.argv[2]))
    except IndexError as i:
        pass
    except Exception as e:
        pass


if __name__ == "__main__":
    main(sys.argv[1:])
# print(fc.get_species())
