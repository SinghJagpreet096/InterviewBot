from dataclasses import dataclass

@dataclass
class Config:
    # Database configuration
    model_id: str = "llama3.2:1b"
    embedder_id: str = "nomic-embed-text"