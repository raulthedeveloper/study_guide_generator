## Will contain Tinker Ui
from cProfile import label
from ctypes import resize
from doctest import testmod
from turtle import width

from pypandoc import convert
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

    file_path_1 = StringVar()
    file_path_2 = StringVar()


    
   
    def labels(self):
        label1 = Label(self.frame, 
                  text = "Questions").place(x = self.width/2 - 120,
                                           y = 100) 
        

        label2 = Label(self.root, 
                  text = "PowerPoint").place(x = self.width/2 - 120,
                                           y = 150)

    def form_fields(self):
        textBox1 = Entry(text="Placeholder text")
        textBox2 = Entry(text="Placeholder text")
        

        textBox1.place(x=self.width/2 - 50, y=100)
        textBox2.place(x=self.width/2 -50, y=150)


    def button(self):
        btn = Button(self.frame, text="Start", command=self.start_program)   
        btn.grid(row=2,column=2,pady=2)

    def generate_listbox(self):
        btn = Button(self.frame, text="Generate Keyword List", command=self.keyword_listbox)   
        btn.grid(row=2,column=1,pady=2)


    def keyword_listbox(self):
        convert =  Convert(self.get_paths()['wordPath'],self.get_paths()['pptPath'])

        listbox = Listbox(self.frame,width = 75)
        listbox.grid(column=1,row=4,pady=10)

        for item in convert.convert_from_word():
            # convert sentences into word and do it one sentence at a time
            listbox.insert(END,item)
            print(item)
        

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
        self.files_selected1(self.word_files)
        self.files_selected2(self.ppt_files)
        self.generate_listbox()
        
        self.root.geometry(f"{self.height}x{self.width}")
        self.root.title("Study")
        self.root.config(bg="#e0e0e0")        
       
        # self.labels()
        
        self.button()


        
        

        self.root.mainloop() 