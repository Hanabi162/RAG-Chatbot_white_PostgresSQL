---

# RAG Chatbot Project

A step-by-step overview of a Retrieve-and-Generate (RAG) chatbot using PostgreSQL + pgvector, Ollama LLM, and a Tkinter GUI.

---

## Requirements
Before starting, make sure you have the following installed:

- [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) (v14+ recommended)  
- [Ollama](https://ollama.com/) (for running a local LLM)  
- Python 3.10+ and the following Python packages:
  - `psycopg2`
  - `numpy`
  - `sentence-transformers`
  - (`tkinter` is usually bundled with Python)

You can install the required Python packages with:
```bash
pip install psycopg2 numpy sentence-transformers
```

> **Note:**  
> - `requests` and `tqdm` are **not required** for this project based on the current codebase.
> - Make sure PostgreSQL server is running and pgvector is properly installed before proceeding.

---

## 1. Overview
- Store document embeddings in PostgreSQL with pgvector  
- Retrieve top-k matches via vector similarity search  
- Generate answers using a local Ollama LLM  
- Interact through a simple Tkinter-based chat interface  

## 2. Install pgvector
- **Docker**: Pull and run the [`pgvector/pgvector`](https://hub.docker.com/r/pgvector/pgvector/tags) image (bundles PostgreSQL and pgvector).  
- **Manual**: Clone the [pgvector GitHub repository](https://github.com/pgvector/pgvector) and run:
  ```bash
  make
  make install
  ```
  to build and install the extension.

## 3. Enable Extension and Define Schema
- Enable the extension inside your database:
  ```sql
  CREATE EXTENSION IF NOT EXISTS vector;
  ```
- Create a `documents` table:
  ```sql
  CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding VECTOR(<dimension>)  -- e.g., VECTOR(1024)
  );
  ```

## 4. RAG Workflow
1. **Ingest**: Encode documents into 1024-dimensional float vectors and store them in the `documents` table.  
2. **Query**: Encode a user's question into a query vector.  
3. **Search**: Perform a nearest-neighbor search using SQL operators (`<->`, `<=>`, `<#>`, `<+>`) to find the top-k matching documents.  
4. **Generate**: Concatenate retrieved snippets and pass them to Ollama to generate a context-grounded answer.

## 5. Project Modules
- **add.py**: Insert text documents and their embeddings into the database.  
- **brain.py**: Core RAG logic — retrieve relevant documents (`query_postgresql`) and generate responses (`generate_response`).  
- **delete.py**: Remove documents by ID or custom criteria.  
- **create_table.py**: Initialize the `documents` table schema.  
- **config.py**: Load environment variables and initialize database connections and the embedder model.  
- **chatbot.py**: Tkinter-based GUI for sending user queries and displaying bot responses.

## 6. Key Concepts
- **Vector Storage**: pgvector enables efficient storage and indexing of high-dimensional arrays.  
- **Similarity Search**: SQL operators calculate distances (Euclidean, cosine, inner-product, or Manhattan) between vectors.  
- **RAG Pattern**: Retrieve relevant context → Generate an informed, grounded answer.

## 7. Getting Started
- Populate your vector database using `add.py`.  
- Launch the Tkinter chat client with `chatbot.py`.  
- Ask questions and receive contextually accurate responses in real time.

---

This project demonstrates a clean, modular RAG architecture using fully local components — ideal for building private, efficient, and extensible AI chatbots.

---
