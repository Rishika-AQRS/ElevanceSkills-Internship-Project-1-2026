# ElevanceSkills-Internship-Project-1-2026
Internship project repository featuring a suite of LLM-based applications (Project: Learn to Build a Real-Time Gen AI Customer Service Bot), including RAG-based knowledge-updatable chatbots, multi-modal systems, and domain-specific expert agents. Built using Python, LangChain, FAISS, and Gemini

# 🚀 Internship Project: Knowledge-Updatable Chatbot (Vector Database)

This project is the implementation of **Task 1** for the Elevance Skills internship. It features a RAG (Retrieval-Augmented Generation) pipeline that allows the chatbot to dynamically update its knowledge base using local text sources.

---

## 🛠 Project Architecture
| Component | Technology |
| :--- | :--- |
| **Orchestration** | LangChain |
| **Vector Store** | FAISS |
| **Embeddings** | `all-MiniLM-L6-v2` |
| **LLM** | Google Gemini (`gemini-flash-latest`) |
| **Frontend** | Streamlit |

---

## 📸 Demonstration

![ChatBot UI (1)](D:\Users\Rishika\Internship1\assets\Chat_Demo_1.png)
![ChatBot UI (2)](D:\Users\Rishika\Internship1\assets\Chat_Demo_2.png)

*Streamlit interface responding to queries based on dynamically ingested files.*

---

## 💡 How it works
1. **Dynamic Ingestion:** Place new `.txt` files in the `/sources` directory.
2. **Indexing:** Running `update_knowledge.py` chunks the text and updates the `FAISS` vector database.
3. **Retrieval:** When a user queries, the system fetches relevant chunks and generates a grounded response using Gemini.
4. **Automation:** `scheduler.py` ensures the database remains fresh without manual intervention.

---

## 🚀 Setup & Execution
1. Install requirements: `pip install -r requirements.txt`
2. Set your Google API Key: `export GOOGLE_API_KEY="your_key"`
3. Update knowledge: `python update_knowledge.py`
4. Run App: `streamlit run app.py`

---

## 📝 Internship Report Summary
* **Skills Learned:** RAG architecture, vector search, Streamlit UI, automated task scheduling.
* **Challenges:** Resolved import issues with LangChain's modular structure and managed API quota limits by switching to the Gemini free-tier model.
