# 📚 Customer Support AI System

This project implements an **AI-powered multi-agent customer support system** using document parsing, hybrid search (semantic + keyword), and LLM-driven dynamic response generation.  
It leverages **Google Gemini API** and **Semantic Kernel** to handle both **technical** and **billing** queries intelligently.

---

## 🚀 Features
- 🔍 PDF Document Parsing and Section Extraction
- 🧠 Sentence Embeddings and Semantic Search
- 🔄 Query Expansion for Better Recall
- 🤖 Multi-Agent Response Generation (Support Agent, Billing Agent)
- 🗺️ Dynamic Agent Selection via Semantic Kernel's Planner
- 🧠 Gemini API integration for LLM-based responses
- 📈 Modular and Scalable Codebase

---

## 📄 How It Works
1. **Document Upload**  
   Upload technical and billing manuals (PDFs). The documents are parsed into sections and converted into vector embeddings.

2. **Query Handling**  
   A customer query is received. The system uses a hybrid search (semantic + keyword) to retrieve relevant sections from the documents.

3. **Dynamic Agent Invocation**  
   Semantic Kernel’s **Sequential Planner** decides whether a **Support Agent** or **Billing Agent** should handle the query.

4. **Response Generation**  
   The selected agent, using the Gemini API, generates a structured, professional, and contextually rich response.

---

## 🧩 Technologies Used
- Python 3.10+
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel)
- [Google Gemini API (Generative AI)](https://ai.google.dev/)
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Scikit-learn (cosine similarity)
- PyPDF2 (PDF parsing)

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/CustomerSupportAI.git
   cd CustomerSupportAI
   ```

2. **Create a virtual environment and activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Google Gemini API Key**
   Update your API key in `services/gemini_chat_service.py`:
   ```python
   genai.configure(api_key="YOUR_API_KEY_HERE")
   ```

5. **Place your PDF documents**
   Put your technical and billing PDFs in an accessible folder. Update the paths in `main.py` accordingly.

6. **Run the application**
   ```bash
   python main.py
   ```

---

## 📝 Example Queries
- _"I was charged twice for AWS service. How can I get a refund?"_
- _"Dashboard widgets not loading after system upgrade."_
- _"Failed to upload files larger than 500MB."_

---

## 📌 Future Enhancements
- Streamlit or FastAPI Web Interface
- Persistent Vector Database (e.g., FAISS or ChromaDB)
- Multi-Document Type Support (Word, HTML)
- Logging and Monitoring
- Conversation Memory Management

---

## 📜 License
This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

