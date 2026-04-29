import streamlit as st
from data_loader import load_xml
import spacy
from spacy import displacy
import scispacy
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

st.title("MedBot: Specialized Medical Questions and Answers")


@st.cache_resource
def load_models():
    nlp=spacy.load("en_core_sci_sm")
    embedder=SentenceTransformer('all-MiniLM-L6-v2')
    return nlp, embedder
nlp, embedder=load_models()

folder_path=r"D:\Users\Rishika\Internship1\Task-3\data\4_MPlus_Health_Topics_QA"
docs=load_xml(folder_path)

if not docs:
    st.error("No data found! Please check your folder path.")
    st.stop()

@st.cache_resource
def build_index(data):
    embeddings=embedder.encode(data)
    dimension=embeddings.shape[1]
    index=faiss.IndexFlatL2(dimension)
    index.add(embeddings.astype('float32'))
    return index

index=build_index(docs)

query=st.text_input("Ask a Medical Question:")

if query:
    doc=nlp(query)
    entities=[ent.text for ent in doc.ents]
    if entities:
        st.write(f"## **Medical Terms Indentied:** {', '.join(entities)}")
    if doc.ents:
        html=displacy.render(doc, style="ent", page=True)
        st.write("### Medical Entity Breakdown: ")
        st.components.v1.html(html, height=200)
    vectors=embedder.encode([query]).astype('float32')
    distance, indices=index.search(vectors, k=1)
    st.write("### Recommended Response: ")
    st.write(docs[indices[0][0]])