from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def generate_summary(text):
    chunk = text[:1024]
    input_len = len(chunk.split())

    # Adjust max_length dynamically
    max_len = min(130, max(30, input_len - 10))

    summary = summarizer(chunk, max_length=max_len, min_length=30, do_sample=False)
    return summary[0]['summary_text']