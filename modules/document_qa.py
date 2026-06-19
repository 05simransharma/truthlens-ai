from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import fitz  # PyMuPDF
from utils.ollama_client import generate_ollama

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
def extract_document(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    return text
def chunk_document(
    text,
    chunk_size=500
):

    chunks = []

    for i in range(
        0,
        len(text),
        chunk_size
    ):
        chunks.append(
            text[i:i + chunk_size]
        )

    return chunks
def create_vector_store(chunks):

    embeddings = embedding_model.encode(
        chunks
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        np.array(
            embeddings,
            dtype=np.float32
        )
    )

    return index, chunks
def retrieve_chunks(
    question,
    index,
    chunks,
    k=3
):

    query_embedding = embedding_model.encode(
        [question]
    )

    distances, indices = index.search(
        np.array(
            query_embedding,
            dtype=np.float32
        ),
        k
    )

    results = []

    for idx in indices[0]:
        results.append(
            chunks[idx]
        )

    return results
def ask_document(
    question,
    index,
    chunks
):

    context_chunks = retrieve_chunks(
        question,
        index,
        chunks
    )

    context = "\n\n".join(
        context_chunks
    )

    prompt = f"""
You are a document assistant.

Answer ONLY using the
provided context.

Context:

{context}

Question:

{question}
"""

    return generate_ollama(
        prompt
    )
