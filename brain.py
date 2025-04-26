import ollama
from config import embedder,conn,k_limit

# Function to search documents
def query_postgresql(query_text, k=k_limit):
    query_embedding = embedder.encode(query_text).tolist()
    cur = conn.cursor()
    sql_query = """
        SELECT content, embedding <=> %s::vector AS similarity_score
        FROM documents
        ORDER BY similarity_score ASC
        LIMIT %s;
    """
    cur.execute(sql_query, (query_embedding, k))
    results = cur.fetchall()
    cur.close()
    return results

# Function to generate a response from the chatbot based on the answer from VectorDB
def generate_response(query_text):
    retrieved_docs = query_postgresql(query_text)
    context = "\n".join([doc[0] for doc in retrieved_docs])
    prompt = f"Answer the question based on the following context:\n{context}\n\nQuestion : {query_text}"
    response = ollama.chat(model="llama3.2", messages=[
        {"role": "system", "content": "You are a female assistant. Answer every response politely and end your answer with 'นะคะ'."},
        {"role": "user", "content": prompt}
    ])
    return response["message"]["content"]