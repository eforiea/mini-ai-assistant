import chromadb
import embedding

client = chromadb.PersistentClient(path="chroma_db")

collections = client.list_collections()

if any(c.name == "company_docs" for c in collections):
    client.delete_collection("company_docs")

collection = client.get_or_create_collection(
    name="company_docs"
)

chunks = []

try:
    with open("documents/company_docs.txt", "r") as docs:

        for doc in docs:

            chunks.append(doc)


except Exception as e:

    print(type(e))

documents = chunks

ids = [f"doc_{i}" for i in range(len(documents))]

embeddings = embedding.embed(documents)

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=ids
)

print("Documents added successfully!")