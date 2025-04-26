from config import cur, conn

# --- Function to delete documents ---
cur.execute("DELETE FROM documents WHERE id = %s", (6,))
conn.commit()
