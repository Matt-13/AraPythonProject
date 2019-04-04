# Ignore errors below this line.
import sys
import cmd
from pythonscripts.FileController import FileController
from pythonscripts.FileView import FileView

# Execute code here
# Matthew Whitaker's code.
fv = FileView()
fc = FileController()


# 4/04/19 Code passes the PEP8 Check.
# CMD based code - Matt


class Main(cmd.Cmd):
    def __init__(self):
        super(Main, self).__init__()
        self.intro = \
            "===============================================\n" \
            "PlantUML to Python Converter\n" \
            "Please type 'help' for all available commands.\n" \
            "Please type 'allhelp' to view the help file.\n" \
            "To continue with a default graph.txt in the\n" \
            "root directory, press [Enter]\n" \
            "=============================================="

    # CMD - Matt
    def cmdloop(self, intro=None):
        print(self.intro)
        while True:
            try:
                super(Main, self).cmdloop(intro="")
                break
            except KeyboardInterrupt:
                print("Ctrl + C pressed, but ignored. "
                      "Please use 'exit' or 'quit' "
                      "to stop the program.")
            except TypeError and ValueError:
                fv.general_error()
                print("Please verify your command, and try again.")
            except Exception:
                fv.general_error()
                print("An error has occurred.")

    # Continues when no command is entered - Matt
    def emptyline(self):
        fv.fe_defaults()
        fc.handle_command('', '')

    # Load method - Matt
    def do_load(self, line):
        """
        LOADS your SOURCE PlantUML text file, and translates it
        into a python file, from the current working directory.
        Usage: LOAD [filename.txt]
        """
        fc.handle_command("load", line)
        fv.next_command()

        """
        userinput = input("Would you like to view the file? (Y/N) ")
        if userinput.lower() == "y":
            # open the file
            pass
        elif userinput.lower() == "n":
            pass
        else:
            # ask them again
            pass
        """

    # Absload method - Matt
    def do_absload(self, line):
        """
        LOADS your SOURCE PlantUML text file, and translates it
        into a python file, from the directory of your choosing.
        Usage: ABSLOAD [path_to_filename.txt]
        """
        if "\\" in line:
            fc.handle_command("absload", line)
            fv.next_command()
        else:
            fv.general_error()
            fv.fe_abs_path_error()
            fv.next_command()

    # View help file - Matt and Liam
    def do_allhelp(self, line):
        """
        SHOWS all HELP relating to this program.
        Usage: ALLHELP
        """
        fv.print_help()
        fv.next_command()

    # Exit method - Matt
    def do_exit(self, line):
        """
        EXITS the program cleanly. (same as QUIT)
        Usage: exit
        """
        exit()

    # Quit method - Matt
    def do_quit(self, line):
        """
        QUITS the program cleanly. (same as EXIT)
        Usage: quit
        """
        self.do_exit(line)

    # Save method - Liam
    def do_save(self, line):
        """
        Saves the converted plantuml code from the database to a textfile
        Usage: save {filename.txt} {code_id}
        """
        line = line.split(' ')
        fc.save_file(line[0], line[1])
        fv.next_command()

    # Printcode method - Liam
    def do_printcode(self, line):
        """
        Prints the converted plantuml code from the database to the cmd
        Usage: printcode {code_id}
        """
        fc.print_code(line)
        fv.next_command()

    # Loadcode method - Liam
    def do_loadcode(self, line):
        """
        Loads code from the database into self.data
        Usage: loadcode {code_id}
        """
        fc.load_code(line)
        fv.next_command()

    # Printfile method - Liam
    def do_printfile(self, line):
        """
        Prints the data saved inside self.data to the cmd
        Usage: printfile
        """
        fc.print_file()
        fv.next_command()


# Liam
def print_to_screen():
    their_answer = input("Would you like to print the "
                         "code to the screen? y/n: ")
    if their_answer == "y":
        fc.print_file()

    their_answer = input("Would you like to save the code to Output.txt y/n: ")
    if their_answer == "y":
        fc.save_file("Output.txt")


m = Main()


if __name__ == "__main__":
    # For Debugging Sys.Argv
    # print('Number of arguments:', len(sys.argv), 'arguments.')
    # print('Argument List:', str(sys.argv))
    if len(sys.argv) >= 2:
        command = str(sys.argv[1]).lower()
    try:
        if len(sys.argv) < 2:
            m.cmdloop()
            # fv.fe_defaults()
            # fc.handle_command('', '')
            # print_to_screen()
        elif len(sys.argv) > 3:
            # Liam's save command
            if command == "save":
                if len(sys.argv) == 2:
                    fv.general_error()
                    fv.fe_command_syntax("Save")
                else:
                    fc.save_file(sys.argv[2], sys.argv[3])
            else:
                fv.fe_too_many_args()
        else:
            if command == "help":
                fc.view_help()

            # Liam's save command
            elif command == "save":
                if len(sys.argv) == 2:
                    fv.general_error()
                    fv.fe_command_syntax("Save")
                else:
                    fc.save_file(sys.argv[2], sys.argv[3])

            # Liam's loadcode command
            elif command == "loadcode":
                if len(sys.argv) == 2:
                    fv.general_error()
                    fv.fe_loadcode_syntax("loadcode")
                else:
                    fc.load_code(sys.argv[2])

            # Liam's printcode command
            elif command == "printcode":
                if len(sys.argv) == 2:
                    fv.general_error()
                    fv.fe_loadcode_syntax("printcode")
                else:
                    fc.print_code(sys.argv[2])

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
    else:
        pass
        # m.cmdloop()
