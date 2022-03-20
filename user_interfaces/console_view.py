## Console interface 
from program import Program

class Console_UI:
    
    @staticmethod
    def welcome():
        print("Welcome to study app please follow the instructions below")

    @staticmethod
    def menu_1():
        print("What is the first file")
        input_1 = input()

        print("What is the second file")
        input_2 = input()

        program = Program(input_1,input_2)

        program.start_program()



    def start_console_ui(self):
        Console_UI.welcome()
        Console_UI.menu_1()