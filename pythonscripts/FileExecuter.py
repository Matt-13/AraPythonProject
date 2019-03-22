# Ignore errors below this line.
import sys
from FileController import FileController
from FileView import FileView

# Execute code here
# Matthew Whitaker's code.
fc = FileController()


def main(argv):

    # For Debugging Sys.Argv
    # print('Number of arguments:', len(sys.argv), 'arguments.')
    # print('Argument List:', str(sys.argv))
    inputfile = ''
    try:
        if len(sys.argv) < 2:
            print("\nNo arguments entered.. "
                  "Continuing with defaults.")
            fc.handle_command('', '')
            #print_to_screen()
        if len(sys.argv) > 3:
            print("\nToo many arguments entered. "
                  "Please enter at most 2.")
        else:
            if str(sys.argv[1]) == "help":
                fc.view_help()

            elif str(sys.argv[1]) == "save":
                if len(sys.argv) == 2:
                    print("\n=======ERROR=======\n"
                          "Syntax Error:\n"
                          "Load requires a file to save to.\n"
                          "Syntax: save {file.txt}")
                else:
                    fc.save_file(sys.argv[2])

            elif str(sys.argv[1]) == "load":
                if len(sys.argv) == 2:
                    print("\n=======ERROR=======\n"
                          "Syntax Error:\n"
                          "Load requires a file to load.\n"
                          "Syntax: load {file.txt}")
                else:
                    fc.handle_command("load", str(sys.argv[2]))
            elif str(sys.argv[1] == "lload"):
                if len(sys.argv) == 2:
                    print("\n=======ERROR=======\n"
                          "Syntax Error:\n"
                          "Lload requires a file to load.\n"
                          "Syntax: lload {path_to_file.txt}")
                if "\\" in str(sys.argv[2]):
                    fc.handle_command("lload", str(sys.argv[2]))
                else:
                    print("\n=======ERROR=======\n"
                          "Syntax Error:\n"
                          "Path must be an absolute path.")
    except IndexError as i:
        pass
    except Exception as e:
        pass
    except PermissionError as p:
        print("File Permission Error!"
              "Do you have the correct permission to read the file?"
              + str(p))


def print_to_screen():
    their_answer = input("Would you like to print the code to the screen? y/n: ")
    if their_answer == "y":
        fc.print_file()

    their_answer = input("Would you like to save the code to Output.txt y/n: ")
    if their_answer == "y":
        fc.save_file("Output.txt")


if __name__ == "__main__":
    main(sys.argv[1:])
# print(fc.get_species())
