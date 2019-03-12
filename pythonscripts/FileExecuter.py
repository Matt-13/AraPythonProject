# Ignore errors below this line.
from FileController import FileController


# Execute code here
def main():
    fc = FileController()
    fc.handle_command('--help')


main()
# print(fc.get_species())
