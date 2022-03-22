## Will contain Tinker Ui

from file_handler import File_Handler
from convert_files import Convert
from program import Program
from tkinter import *
import os



class Graphic_UI:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    ##program = Program(file1,file2)
    file_handler = File_Handler()
    ppt_dir_path = f"{os.path.abspath(os.curdir)}\datafiles\powerpoints"
    word_dir_path = f"{os.path.abspath(os.curdir)}\datafiles\word"
    word_files = file_handler.get_file_names(word_dir_path)
    ppt_files = file_handler.get_file_names(ppt_dir_path)
    root = Tk()
    frame = LabelFrame(root,text="Study Guide Builder",padx=50,pady=50)
    keyword_frame = LabelFrame(frame,text="Key Words",padx=5,pady=5)

    current_question = {}
    

    file_path_1 = StringVar()
    file_path_2 = StringVar()


    
   
    def labels(self):
        label1 = Label(self.frame, 
                  text = "Questions") 
        

        label2 = Label(self.frame, 
                  text = "PowerPoint")

        
        
        label1.grid(column=1,row=0,pady=5)
        label2.grid(column=2,row=0,pady=5)
        
    
    def keyword_navigation(self):

        convert =  Convert(self.get_paths()['wordPath'],self.get_paths()['pptPath'])

        index = 0

        def forward():
            nonlocal index
            print("I go forward")
            index += 1
            self.current_question = convert.convert_into_keywords()[index]
            self.keyword_listbox()
            print(self.current_question['words'])
            print("++++++++++++++++++++++++++++++++++++++++++=")

        def backwards():
            nonlocal index
            print("I go backwards")
            index -= 1
            self.current_question = convert.convert_into_keywords()[index]
            self.keyword_listbox()
            print(self.current_question['words'])
            print("++++++++++++++++++++++++++++++++++++++++++=")


        button_frame = Frame(self.keyword_frame,padx=5,pady=5)
        button_frame.grid(row=2,column=1)

        prev = Button(button_frame,text="Prev",command=backwards)
        next = Button(button_frame,text="Next",command=forward)
        count_label = Label(button_frame,text="1 2 3 4")
        count_label.grid(column=1,row=1,padx=10)

        prev.grid(row=1,column=0)
        next.grid(row=1,column=2)



    def button(self):
        btn = Button(self.frame, text="Start", command=self.start_program)   
        btn.grid(row=2,column=2,pady=2)

    def generate_listbox(self):
        btn = Button(self.frame, text="Generate Keyword List", command=self.keyword_listbox)   
        btn.grid(row=2,column=1,pady=2)


    def keyword_listbox(self):
        convert =  Convert(self.get_paths()['wordPath'],self.get_paths()['pptPath'])

        self.current_question = convert.convert_into_keywords()[0]


        listbox = Listbox(self.keyword_frame,width = 75)
        listbox.grid(column=1,row=1,pady=10)
        self.keyword_navigation()


        for item in self.current_question['words']:
            # convert sentences into word and do it one sentence at a time

             listbox.insert(END,item)
        


        # btn.pack(side='bottom')
    def files_selected1(self,OPTIONS):
        self.file_path_1.set(OPTIONS[0])

        w = OptionMenu(self.frame, self.file_path_1, *OPTIONS)
        w.grid(row=1,column=1, pady=2)

        


    def files_selected2(self,OPTIONS):
        self.file_path_2.set(OPTIONS[0])

        w = OptionMenu(self.frame, self.file_path_2, *OPTIONS)
        w.grid(row=1,column=2, pady=2)

        

    def get_paths(self):   
        filepaths = {
           'wordPath':f"{self.word_dir_path}//{self.file_path_1.get()}",
           'pptPath': f"{self.ppt_dir_path}//{self.file_path_2.get()}"
        }
        return filepaths


    def start_program(self):
        program = Program(self.get_paths()['wordPath'],self.get_paths()['pptPath'])

        program.start_program()
        

    def run(self):
        self.frame.pack(pady=75)

        self.keyword_frame.grid(column=1,row=5)
        

        self.labels()
        self.files_selected1(self.word_files)
        self.files_selected2(self.ppt_files)
        self.generate_listbox()
        

        
        self.root.geometry(f"{self.height}x{self.width}")
        self.root.title("Study")
        self.root.config(bg="#e0e0e0")        
       
        # self.labels()
        
        self.button()


        
        

        self.root.mainloop() 