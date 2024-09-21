from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)

class ChatHistory:
    def __init__(self, session_id: str):
        self.history = {}
        self.session_id = session_id

    def get_session_history(self) -> BaseChatMessageHistory:
        if self.session_id not in self.history:
            self.history[self.session_id] = InMemoryChatMessageHistory()
        return self.history[self.session_id]
    
    