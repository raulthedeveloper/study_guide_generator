## Converts select files into text files to be parsed over

import collections 
import collections.abc
from pptx import Presentation

import pypandoc



class Convert:

    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
      

    def test(self):
        print("test is working")

    def convert_from_pdf(self):
        return 0

    def convert_from_word(self):
        output = pypandoc.convert_file(self.file1, 'txt', outputfile="somefile.txt")
        assert output == ""
        

    def convert_from_powerpoint(self):
        prs = Presentation(self.file2)
        text_runs = []

        for slide in prs.slides:
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        text_runs.append(run.text)
        print(text_runs)

    def create_word_doc(self):
        #Will be used to results back into a word document
        return 
