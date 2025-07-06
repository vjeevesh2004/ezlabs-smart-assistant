import streamlit as st
from backend.utils import load_document
from backend.summarizer import generate_summary
from backend.qna_handler import ask_question
from backend.challenge_mode import generate_questions, evaluate_answer

st.set_page_config(
    page_title="Smart Assistant",
    layout="centered"
)

# background & text colours
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #f7f9fc;
            color: #000000;
        }
        .stTextInput > label, .stFileUploader > label, .stRadio > div {
            color: #000000 !important;
        }
        section[data-testid="stSidebar"] {
            width: 220px !important;
        }
        div[class*="stAlert"] {
            background-color: #fff6bf !important;
            color: #000000 !important;
            border: 1px solid #fdd835 !important;
            font-weight: 500 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#4B8BBE; margin-top: -40px;'>Smart Research Assistant</h1>", unsafe_allow_html=True)
st.write("This tool reads your document and lets you ask or answer questions based on it.")

# Sidebar for mode selection
st.sidebar.title("🧠 Assistant Panel")
mode = st.sidebar.radio("Choose Interaction Mode", ["Ask Anything", "Challenge Me"])
# st.sidebar.info("💡 Tip: Upload a DSA syllabus, resume, or question paper to begin!")

# Upload section
st.header("Upload Document")
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    text = load_document(uploaded_file)
    st.success(f"Uploaded: {uploaded_file.name}")

    # Summary section
    st.header("Auto Summary")
    summary = generate_summary(text)
    st.write(summary)

    # Interaction section
    st.header("Interact with Document")

    if mode == "Ask Anything":
        question = st.text_input("Ask a question based on the document:")
        if question:
            answer, reference, confidence = ask_question(question, text)
            if confidence < 0.2:
                st.warning("The answer may be unreliable or unrelated. Try rephrasing your question.")
            st.write("**Answer:**", answer)
            st.caption(f"Reference: {reference} | Confidence: {confidence:.2f}")

    elif mode == "Challenge Me":
        st.write("Answer the following questions:")
        questions = generate_questions(text)
        for i, q in enumerate(questions):
            user_answer = st.text_input(f"Q{i+1}: {q}", key=f"q_{i}")
            if user_answer:
                feedback = evaluate_answer(q, user_answer, text)
                st.write("Feedback:", feedback)

    st.markdown("""
                ---
                <p style='text-align:center; font-size: 14px;'>
                Built by <strong>Jeevesh Varshney</strong><br>
                B.Tech CSE (Data Science), RKGIT
                </p>
                """, unsafe_allow_html=True)

else:
    st.warning("Please upload a document to get started.")
