## Will contain Tinker Ui
from cProfile import label
from file_handler import File_Handler
from program import Program
from tkinter import *



class Graphic_UI:

    

    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    ##program = Program(file1,file2)
    file_handler = File_Handler()
    ppt_dir_path = "C:\\Users\\raul_\\Desktop\\Projects\\Study App\datafiles\powerpoints"
    word_dir_path = "C:\\Users\\raul_\\Desktop\\Projects\\Study App\datafiles\word"
    word_files = file_handler.get_file_names(word_dir_path)
    ppt_files = file_handler.get_file_names(ppt_dir_path)
    root = Tk()

    file_path_1 = StringVar()
    file_path_2 = StringVar()


   
    def labels(self):
        label1 = Label(self.root, 
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
        # btn = Button(self.root, text="Start", command=self.program.start_program)   
        btn = Button(self.root, text="Start", command=self.create_path)  
        btn.place(x = self.width/2, y = self.height/2)

        # btn.pack(side='bottom')
    def files_selected1(self,OPTIONS):
        variable = StringVar(self.root)
        variable.set(OPTIONS[0]) # default value

        w = OptionMenu(self.root, self.file_path_1, *OPTIONS)
        w.pack()

        


    def files_selected2(self,OPTIONS):
        variable = StringVar(self.root)
        variable.set(OPTIONS[0]) # default value

        w = OptionMenu(self.root, self.file_path_2, *OPTIONS)
        w.pack()

        

    def create_path(self):   

        print(f"{self.word_dir_path}//{self.file_path_1.get()}")
        print(f"{self.ppt_dir_path}//{self.file_path_2.get()}")


    
        

    def run(self):
        print("Graphic Ui is working")

        self.files_selected1(self.word_files)
        self.files_selected2(self.ppt_files)
        
        self.root.geometry(f"{self.height}x{self.width}")
        self.root.title("Study")
        self.root.config(bg="#e0e0e0")        


        # self.form_fields()
        # self.labels()
        
        self.button()


        
        

        self.root.mainloop() 