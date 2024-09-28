import streamlit as st
from streamlit import session_state as ss
from model import Model
from utilities import display_message
from chat_history import ChatHistory
from embedding import Embeddings

SESSION_ID = "123"


 
def chat(retriever):
    
    start_interview = st.button("Begin Interview")
    end_interview = st.button("End Interview")
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

# Function to add a new message to the conversation
    def add_message(role, message):
        st.session_state.conversation.append({"sender":role,
                                            "message": message})

    if start_interview:
        # Generate prompt and get questions
        model = Model(session_id=SESSION_ID)
        llm = model.llm
        ch = ChatHistory(session_id=SESSION_ID, llm=llm, retriever=retriever)
        rag_chain = ch.chain()  
        question = model.get_response(rag_chain=rag_chain,session_history=ch.get_session_history , query="")
        print(question)
        add_message("Interviewer", question.content)
    col1, col2 = st.columns([4,1])
    with col1:
        response = st.text_input("", label_visibility="collapsed",placeholder="Type your response here")
    with col2:
        submit = st.button("Submit")
    # Get response
    # if submit:
    #     add_message("Candidate", response)
    #     question = model.get_response(rag_chain=rag_chain,session_history=ch.get_session_history , query=response)
    #     # st.write(questions)
    #     add_message("Interviewer", question.content)


    # if record:
    #     response = speech_to_text()
    #     add_message("Candidate", response)
    #     question = model.chain_response(response,CHAT_HISTORY)
    #     # st.write(questions)
    #     add_message("Interviewer", question.content)
    # for chat in st.session_state.conversation:
    #     display_message(message=chat['message'], sender=chat['sender'])
        
    # if end_interview:
    #     summary = model.get_response(rag_chain=rag_chain,session_history=ch.get_session_history , query="summarize the interview")
    #     st.write(f"Summary:{summary.content}")
    #     st.write("Interview Ended")
    #     st.session_state.conversation = []
        
if __name__ == "__main__":
    
    chat(retriever=ss.retriever)

