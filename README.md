# 🧠 EZ Labs – Smart Research Assistant (Data Science Intern Project)

This Smart Assistant was developed as part of the **EZ Labs Data Science Internship**. It reads PDF/TXT documents, summarizes them, answers user questions, and generates comprehension challenges — all without relying on OpenAI APIs.

---

## 🚀 Features

- 📂 Upload PDF or TXT documents
- ✨ Auto-summary in under 150 words
- 💬 Ask Anything mode (natural language Q&A)
- 🎯 Challenge Me mode (logic-based quiz)
- 🧠 100% local using Hugging Face models (offline-capable)
- 🎨 Light UI with professional touch

---


🛠️ Setup Instructions
🔹 1. Clone the repository
git clone https://github.com/jeeveshvarshney/ezlabs-smart-assistant.git
cd ezlabs-smart-assistant
🔹 2. Install dependencies
pip install -r requirements.txt
🔹 3. Run the app
python -m streamlit run app.py
The app will open at: http://localhost:8501

---


### 🔹 Process Breakdown (Human-Friendly)

1. ✅ User opens the app via Streamlit interface
2. 📄 Uploads a PDF or TXT file
3. 🧹 Document is read and preprocessed
4. 📝 A summary is generated using `t5-small`
5. 💬 User asks questions → answered using `roberta-base-squad2`
6. 🎯 In challenge mode, questions are generated using `flan-t5-base`
7. 📋 User responses are evaluated, and feedback is given

          
---
## 👨‍💻 Author
Name: Jeevesh Varshney
Course: B.Tech CSE (Data Science)
College: Raj Kumar Goel Institute of Technology (RKGIT)
GitHub: github.com/jeeveshvarshney
LinkedIn: linkedin.com/in/jeeveshvarshney
