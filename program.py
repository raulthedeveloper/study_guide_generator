from convert_files import Convert
from file_handler import File_Handler

## Contains all evenhandlers for program




class Program:
    def __init__(self,file1,file2):
        self.file1 = file1
        self.file2 = file2
        
    
    def get_file_1(self):
        return self.file1
    
    def get_file_2(self):
        return self.file2

    def start_program(self):
        print("Program is running")

        convert = Convert(self.file1,self.file2)
        create_dir = File_Handler()
        
        create_dir.check_if_exists()

        convert.convert_from_powerpoint()