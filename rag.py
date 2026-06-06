import chromadb
from sentence_transformers import SentenceTransformer

# Load the embedding model (converts text to searchable meaning)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Create a local ChromaDB database
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="it_docs")

def load_docs(filepath):
    """Read the IT docs and split into chunks"""
    with open(filepath, "r") as f:
        text = f.read()
    
    # Split by double newline into sections
    chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
    
    # Add chunks to ChromaDB
    embeddings = embedder.encode(chunks).tolist()
    
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )
    
    print(f"✅ Loaded {len(chunks)} chunks from docs\n")

def search_docs(query, n_results=2):
    """Search docs for the most relevant chunks"""
    query_embedding = embedder.encode([query]).tolist()
    
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )
    
    # Return the most relevant chunks as a single string
    return "\n\n".join(results["documents"][0])

# Load docs when this file is imported
load_docs("it_docs.txt")