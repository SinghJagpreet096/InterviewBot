from llama_index.core import SimpleDirectoryReader

# load data

class DocumentReader:
    def __init__(self, input_dir, required_exts:list, recursive:bool=False):
        self.input_dir = input_dir
        self.required_exts = required_exts
        self.recursive = recursive
        self.loader = SimpleDirectoryReader(
            input_dir=self.input_dir,
            required_exts=required_exts,
            recursive=recursive
        )

    def get_chunks(self):
        return self.loader.load_data()

if __name__ == "__main__":
    reader = DocumentReader(
        input_dir="/Users/jagpreetsingh/ML_Projects/interviewbot/",
        required_exts=[".pdf"],
        recursive=False
    )

    chunks = reader.get_chunks()

    print(chunks)