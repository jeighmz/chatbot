from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st


st.title("Langchain-LLama3 app")

template = """<system>You are an expert at solving problems. Any problem you got it. You must answer the question to the best of your ability</system>: 
        <question>
            {question}
        </question>
"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3")

chain = prompt | model

question = st.chat_input("Enter your question here: ")
if question: 
    st.write(chain.invoke({"question": question}))