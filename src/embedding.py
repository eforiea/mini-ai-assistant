from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2", local_files_only=True)

def embed(text):

    embedding = model.encode(text).tolist()

    return embedding