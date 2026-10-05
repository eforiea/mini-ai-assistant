import chromadb
import sys
import llm
import embedding

client = chromadb.PersistentClient("chroma_db")

try:

    collection = client.get_collection(name="company_docs")

except Exception as e:

    print("ERROR: Collection 'company_docs' not found.")
    print("Run vector_store.py first.")
    sys.exit(1)



def search(query_embedding):

    results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
    )

    return results



def rag(user_input):

    query_embedding = embedding.embed(user_input)

    results = search(query_embedding)

    context = "\n".join(results["documents"][0])

    prompt = f"""
Use the retrieved context if it is relevant.
If the context does not answer the question, use your general knowledge.

Context:
{context}

Question:
{user_input}
"""

