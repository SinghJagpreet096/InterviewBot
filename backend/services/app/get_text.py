import PyPDF2
from typing import TextIO, BinaryIO

class GetText:
    def pdf(self, file:BinaryIO) -> str: 
        reader = PyPDF2.PdfReader(file)
        text = ""
    
        # Iterate through all the pages
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text
    
    def docx(self, file:TextIO) -> str:
        pass

if __name__ == "__main__":
    get_text = GetText()
    print(get_text.pdf("/Users/jagpreetsingh/ML_Projects/interviewbot/1724448810.pdf"))