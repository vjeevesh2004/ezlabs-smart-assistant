from transformers import pipeline

# Load flan-t5 model
flan = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_questions(context):
    prompt = f"""Generate 3 logical and comprehension-based questions from the following text. Avoid vague or definition-style questions.

Document:
\"\"\"
{context[:800]}
\"\"\"

Return each question as a numbered list.
"""
    output = flan(prompt, max_length=256, clean_up_tokenization_spaces=True)[0]['generated_text']
    
    # Clean output and extract questions
    questions = []
    for line in output.split("\n"):
        line = line.strip()
        if line and (line[0].isdigit() or line.startswith("-")):
            q = line.split(". ", 1)[-1].strip("- ").strip()
            questions.append(q)

    return questions[:3]

def evaluate_answer(question, user_answer, context):
    prompt = f"""Evaluate the following answer based on the provided document. Give clear feedback on correctness with short justification.

Question: {question}
User's Answer: {user_answer}

Document:
\"\"\"
{context[:1000]}
\"\"\"

Respond in this format:
Correctness: ✅ or ❌
Feedback: <explanation>
"""
    output = flan(prompt, max_length=256, clean_up_tokenization_spaces=True)[0]['generated_text']
    return output.strip()