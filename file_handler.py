# Generate folder structure for app.
import os


class File_Handler:
        

    def create_directory():
        os.makedirs('datafiles/powerpoints')
        os.makedirs('datafiles/results')
        os.makedirs('datafiles/word')

    def get_file_names(self,path):
        if os.path.exists(path):
            dir_list = os.listdir(path)
        else:print("Path does not exist")
        
        
        # print the list
        return dir_list  
    
    def check_if_exists(self):
        if(os.path.exists("datafiles") == False):
           self.create_directory()
        
    
   

    
    