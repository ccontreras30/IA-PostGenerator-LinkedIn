from transformers import pipeline

resumidor = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def resumir(texto):
    return resumidor(texto[:1000])[0]["summary_text"]
