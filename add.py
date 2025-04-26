from config import conn, cur, embedder

# --- Function to add a document ---
def add_document(text):
    embedding = embedder.encode(text).tolist()
    cur.execute(
        "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
        (text, embedding)
    )
    conn.commit()

# --- Document data ---
documents = [
    """ 
        Please enter the document you want, such as relevant information.
    """
]

for doc in documents:
    add_document(doc)

cur.close()
conn.close()
