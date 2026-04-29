# MedBot: Specialized Medical Q&A Chatbot

This project is a part of my ElevanceSkills Internship Project and it demonstrates the RAG and NER capabilities using the MedQuAD dataset.
MedBot is a specialized medical question-answering system developed using the MedQuAD dataset. It utilizes semantic search and natural language processing to provide accurate medical information.

## Features
- **Retrieval-Augmented Generation (RAG):** Uses FAISS and SentenceTransformers for efficient and accurate document retrieval.
- **Medical Entity Recognition (NER):** Leverages scispaCy (en_core_sci_sm) to identify medical symptoms, diseases, and treatments in user queries.
- **Interactive UI:** A clean, user-friendly interface built with Streamlit.

## Setup Instructions

1. **Clone the repository** and navigate to the project directory.

2. **Install core dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install the scispaCy model:**
   ```bash
   pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz
   ```

## How to Run
1. Ensure your MedQuAD data is placed in the `data/` folder.
2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Dataset Source
This project uses the [MedQuAD dataset](https://github.com/abachaa/MedQuAD).