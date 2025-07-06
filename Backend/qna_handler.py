from transformers import pipeline

qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")

def ask_question(question, context):
    try:
        context_window = context[:3000]
        result = qa_model(question=question, context=context_window)

        answer = result["answer"]
        score = result["score"]

        # Attempt to find a justification snippet
        start_idx = context_window.find(answer)
        if start_idx != -1:
            justification = context_window[start_idx:start_idx + 300]
        else:
            justification = "Justification snippet not found."

        return answer, justification, score

    except Exception as e:
        return "Could not find an answer.", f"Error: {str(e)}", 0.0