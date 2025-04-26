---

# RAG Chatbot Project

A step-by-step overview of a Retrieve-and-Generate (RAG) chatbot using PostgreSQL + pgvector, Ollama LLM, and a Tkinter GUI.

---

## 1. Overview  
- Store document embeddings in PostgreSQL with pgvector  
- Retrieve top-k matches by vector similarity  
- Generate answers using a local Ollama LLM  
- Interact through a simple Tkinter chat interface  

## 2. Install pgvector  
- **Docker**: Pull and run the `pgvector/pgvector` image (bundles PostgreSQL and pgvector).  
- **Manual**: Clone the [pgvector GitHub repository](https://github.com/pgvector/pgvector) and run `make && make install` to build and install the extension.  

## 3. Enable Extension and Define Schema  
- Run `CREATE EXTENSION IF NOT EXISTS vector;` in your database.  
- Create the `documents` table with:  
  - `id SERIAL PRIMARY KEY`  
  - `content TEXT`  
  - `embedding VECTOR(<dimension>)` (e.g., 1024)

## 4. RAG Workflow  
1. **Ingest**: Encode documents into 1024-dimensional float vectors → store in `documents`.  
2. **Query**: Encode user question into a vector.  
3. **Search**: Perform nearest-neighbor search using SQL operators (`<->`, `<=>`, `<#>`, `<+>`) to retrieve top-k documents.  
4. **Generate**: Concatenate retrieved snippets → pass to Ollama → produce a grounded answer.

## 5. Project Modules  
- **add.py**: Insert text documents and embeddings into the database.  
- **brain.py**: Core logic for document retrieval (`query_postgresql`) and LLM generation (`generate_response`).  
- **delete.py**: Utility to remove documents by ID or criteria.  
- **create_table.py**: Script to initialize the `documents` table schema.  
- **config.py**: Load database credentials from environment variables; initialize `psycopg2` connection and embedding model.  
- **chatbot.py**: Tkinter GUI for chat interaction, sending user queries and displaying bot responses.

## 6. Key Concepts  
- **Vector Storage**: pgvector allows efficient storage and indexing of high-dimensional arrays.  
- **Similarity Search**: SQL operators calculate distances (L2, cosine, inner-product, L1) between vectors.  
- **RAG Pattern**: Retrieve relevant context → Generate an informed answer.

## 7. Getting Started  
- Populate your VectorDB using `add.py`.  
- Launch the chat client with `chatbot.py`.  
- Ask questions and receive context-aware responses in real time.

---

This project demonstrates a clean and modular RAG architecture using fully local components — ideal for building private, efficient, and extensible AI chatbots.

---
