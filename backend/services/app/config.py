from dataclasses import dataclass

@dataclass
class Config:
    # Database configuration
    model_id: str = "llama3.2:1b" #"hf.co/singhjagpreet/Llama-3.2-1B-Instruct-Q8_0-GGUF"
    embedder_id: str = "nomic-embed-text"