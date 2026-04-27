import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS

SOURCE_DIR="sources/"
VSTORE_DIR="embeddings/faiss"

def get_embeddings():
    model_name="all-MiniLM-L6-v2"
    return HuggingFaceBgeEmbeddings(model_name=model_name)

def get_vector_db(embeddings):
    if os.path.exists(VSTORE_DIR):
        return FAISS.load_local(
            VSTORE_DIR,
            embeddings,
            allow_dangerous_deserialization=True,
        )
    sample_text=["init"]
    return FAISS.from_texts(sample_text, embeddings)
def read_text_files(dir_path):
    # Absolute path for debugging
    abs_path = os.path.abspath(dir_path)
    print(f"DEBUG: Looking for files in: {abs_path}")
    
    docs = []
    if not os.path.exists(abs_path):
        print(f"DEBUG: Path {abs_path} does not exist!")
        return docs

    for fname in os.listdir(abs_path):
        print(f"DEBUG: Found file: {fname}") # See what it finds
        if fname.endswith(".txt"):
            path = os.path.join(abs_path, fname)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    docs.append(content)
        else:
            print(f"DEBUG: Skipping {fname} (not a .txt file)")
    return docs

def update_knowledge_base():
    print("Loading Your Embeddings Model....")
    embeddings=get_embeddings()
    print("Creating and Loading Vector Databases....")
    db=get_vector_db(embeddings)
    texts=read_text_files(SOURCE_DIR)
    if not texts:
        print("No Text Files Found in ", SOURCE_DIR)
        return
    print("Grouping Text Into Chunks....")
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )

    docs=splitter.create_documents(texts)
    print(f"Adding {len(docs)} Chunks To Vector Store....")
    db.add_documents(docs)
    db.save_local(VSTORE_DIR)
    print("Knowledge Base Updated Successfully!")

if __name__ == "__main__":
    update_knowledge_base()





