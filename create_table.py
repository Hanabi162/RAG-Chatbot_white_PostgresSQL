from config import cur,conn

# --- Example of creating data in VectorDB ---
cur.execute("""
    CREATE TABLE IF NOT EXISTS documents (
            id SERIAL PRIMARY KEY,
            content TEXT,
            embedding vector(1024)
            )
            """)
conn.commit()
cur.close()
conn.close()