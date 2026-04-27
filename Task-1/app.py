import streamlit as st
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents.stuff import create_stuff_documents_chain
from  langchain_classic.chains import create_retrieval_chain
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()
print("Does OPENAI_API_KEY exist?", "OPENAI_API_KEY" in os.environ)
VECTORSTORE_DIR="embeddings/faiss"
OPENAI_MODEL="gpt-3.5-turbo"

@st.cache_resource
def get_qa_chain():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.load_local(
        VECTORSTORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True,
    )
    retriever = db.as_retriever(search_kwargs={"k": 3})

    # UPDATE:
    llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest", 
    google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    # Create a prompt
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer the question. "
        "If you cannot find the answer in the context, say that you don't know."
        "\n\n{context}"
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    # Modern RAG chains
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    return rag_chain

st.title("Internship Task 1: Knowledge Updatable Chatbot")

qa=get_qa_chain()


if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt :=st.chat_input("Ask a Question: "):
    st.session_state.messages.append({"role":"user", "content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("Assistant"):
        with st.spinner("Thinking..."):
            result=qa.invoke({"input":prompt})
            answer=result["answer"]
            st.markdown(answer)
            st.session_state.messages.append({"role":"Assistant", "content": answer})

