from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
template = """<system>You are an expert at solving problems. Any problem you got it. You must answer the question to the best of your ability</system>: 
        <question>
            {question}
        </question>
"""
prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="llama3.1")
chain = prompt | model
question = input("> Enter your question here: ")
if question: 
    print(chain.invoke({"question": question}))