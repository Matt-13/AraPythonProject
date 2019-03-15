# Ignore errors below this line.
import sys
from FileController import FileController


# Execute code here
def main(argv):
    fc = FileController()
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    inputfile = ''
    try:
        if len(sys.argv) < 2:
            print("No arguments entered.. Continuing with defaults.")
            fc.handle_command('')
        if len(sys.argv) > 2:
            print("Too many arguments entered. Please enter at most 1.")
        else:
            if str(sys.argv[1]) == "help":
                fc.view_help()
            if str(sys.argv[1]) == "load={filename}":
                fc.handle_command("load")
    except IndexError as i:
        pass
    except Exception as e:
        pass


if __name__ == "__main__":
    main(sys.argv[1:])
# print(fc.get_species())
