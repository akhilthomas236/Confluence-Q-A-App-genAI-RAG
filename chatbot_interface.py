import streamlit as st
from langchain import RetrievalQA, Embeddings
import pickle

# Load embeddings
with open("embeddings.pkl", "rb") as f:
    embeddings = pickle.load(f)

# Initialize ChromaDB with embeddings
chromadb = ChromaDB(embeddings)

# Define RetrievalQA
retrieval_qa = RetrievalQA(chromadb)

# Streamlit interface
st.title("Confluence Chatbot")
user_input = st.text_input("Ask a question:")
if user_input:
    embedding_model = Embeddings(model_name="openai-ada-v2")
    query_embedding = embedding_model.create_embedding(user_input)
    relevant_snippets = retrieval_qa.retrieve(query_embedding)
    st.write(relevant_snippets)
