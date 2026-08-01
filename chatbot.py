from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#Creating my prompts
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are helpful assistant. please respond to the questions asked"),
        ("user","question:{question}")
    ]
)

# streamlit framework
st.title('MY GPT')
input_text = st.text_input('what questions do you have in mind')

#Let's create LLM chain system
# ollama LAAMA2 model
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser 

if input_text:
    st.write(chain.invoke({"question":input_text}))
