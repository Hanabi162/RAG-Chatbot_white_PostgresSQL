import tkinter as tk
from tkinter import scrolledtext
from brain import generate_response

# --- GUI page for conversation ---
def ask_question(event=None):  # เพิ่ม event=None ไว้รับ event จากการกดปุ่ม
    user_query = entry.get()
    if not user_query.strip():
        return
    
    # Display user's message
    chat_window.configure(state='normal')
    chat_window.insert(tk.END, f"👤 You: {user_query}\n", "user")
    chat_window.configure(state='disabled')
    chat_window.see(tk.END)

    entry.delete(0, tk.END)

    # Send the user's query to generate_response
    bot_reply = generate_response(user_query)

    # Display bot's message
    chat_window.configure(state='normal')
    chat_window.insert(tk.END, f"🤖 Bot: {bot_reply}\n", "bot")
    chat_window.configure(state='disabled')
    chat_window.see(tk.END)

# --- Main GUI setup ---
root = tk.Tk()
root.title("🧠 RAG Chat")
root.geometry("550x600")
root.configure(bg="white")

# --- Chat Window ---
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), state='disabled')
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_window.tag_configure("user", foreground="blue")
chat_window.tag_configure("bot", foreground="green")

# --- Input Box ---
entry_frame = tk.Frame(root, bg="white")
entry_frame.pack(pady=10, fill=tk.X)

entry = tk.Entry(entry_frame, font=("Arial", 14))
entry.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.X, expand=True)

# Bind Enter key to trigger the send action
entry.bind("<Return>", ask_question)

ask_button = tk.Button(entry_frame, text="ส่งข้อความ", command=ask_question, font=("Arial", 12), bg="#4CAF50", fg="white")
ask_button.pack(side=tk.LEFT, padx=10)

root.mainloop()