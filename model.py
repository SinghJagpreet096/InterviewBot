from meta_ai_api import MetaAI
# from langchain.llms import metaai
import langchain

class Model:
    def __init__(self):
        self.meta_ai = MetaAI()
        # self.llm = metaai()
        # self.conversation = langchain.ConversationManager(self.llm, max_tokens=2048)

    def get_response(self, query):
        response = self.meta_ai.prompt(
            message=query)
        return response['message']
    
    # def chain_response(self, query):
    #     self.conversation.add_user_input(query)
    #     response = self.conversation.get_response()
    #     return response['message']
    
if __name__ == "__main__":
    model = Model()
    query = "What is your name?"
    response = model.chain_response(query)