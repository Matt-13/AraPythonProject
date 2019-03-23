# Ignore errors below this line.
import sys
from pythonscripts.FileController import FileController
from pythonscripts.FileView import FileView

# Execute code here
# Matthew Whitaker's code.
fv = FileView()
fc = FileController()


def main(argv):

    # For Debugging Sys.Argv
    # print('Number of arguments:', len(sys.argv), 'arguments.')
    # print('Argument List:', str(sys.argv))
    if len(sys.argv) >= 2:
        command = str(sys.argv[1]).lower()
    try:
        if len(sys.argv) < 2:
            fv.fe_defaults()
            fc.handle_command('', '')
            # print_to_screen()
        elif len(sys.argv) > 3:
            fv.fe_too_many_args()
        else:
            if command == "help":
                fc.view_help()

            elif command == "save":
                if len(sys.argv) == 2:
                    fv.general_error()
                    fv.fe_command_syntax("Save")
                else:
                    fc.save_file(sys.argv[2])

            elif command == "load":
                if len(sys.argv) == 2:
                    fv.general_error()
                    fv.fe_command_syntax("Load")
                else:
                    fc.handle_command("load", str(sys.argv[2]))
            elif command == "absload":
                if len(sys.argv) == 2:
                    fv.general_error()
                    fv.fe_abs_syntax()
                if "\\" in str(sys.argv[2]):
                    fc.handle_command("absload", str(sys.argv[2]))
                else:
                    fv.general_error()
                    fv.fe_abs_path_error()
            else:
                fv.general_error()
                fv.output("Command not found!")
    # Ignores issues with Sys.argv
    except IndexError:
        pass
    # Checks for file permission errors.
    except PermissionError:
        print("Permission Error!\n"
              "Check you have the permission to read the file!")


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
