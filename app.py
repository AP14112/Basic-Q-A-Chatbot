import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
os.environ["LANGCHAIN_TRACING_V2"] = "true" 
os.environ["LANGCHAIN_PROJECT"]="Q&A chatbot"


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that helps people find information."),
        ("user", "Question:{question}"),
    ]
)

def generate_response(question,api_key,llm_model,temperature,max_tokens):
    model=ChatGroq(model=llm_model,groq_api_key=api_key,temperature=temperature,max_tokens=max_tokens)
    output_parser=StrOutputParser()
    chain=prompt|model|output_parser
    answer=chain.invoke({"question":question})
    return answer

##TITLE OF THE APP
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Groq API Key",type="password")

llm=st.sidebar.selectbox("Select LLM Model",["gemma2-9b-it", "groq/compound"]  )
temperature=st.sidebar.slider("Select Temperature",min_value=0.0,max_value=1.0,value=0.7,step=0.1)
max_tokens=st.sidebar.slider("Select Max Tokens",min_value=50,max_value=400,value=1000,step=150)

st.write("Ask questions about anything and get answers!")
user_input=st.text_input("Enter your question here")

if(user_input and api_key):
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)

else:
    st.write("Please enter your question and Groq API Key to get the answer.")
    