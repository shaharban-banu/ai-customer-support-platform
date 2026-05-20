# from transformers import pipeline

# sentiment_pipeline=pipeline("sentiment-analysis")

#summarizer=pipeline("summarization",model="sshleifer/distilbart-cnn-12-6")

def classify_ticket(message:str):
    text = message.lower()

    if "payment" in text:
        return "billing"

    if "refund" in text:
        return "refund"

    if "login" in text:
        return "account"

    if "delivery" in text:
        return "delivery"

    return "technical"


def analyze_sentiment(message: str):
    negative_words=[
            "bad",
            "terrible",
            "failed",
            "worst",
            "angry",
            "issue",
            "problem",
            "refund",
            "delayed",
            "delay",
            "not received",
            "broken",
            "error",
            "late",
            "complaint"
            ]
    if any(word in message.lower()  for word in negative_words):
        return "Negative"
    return "Positive"

    # result = sentiment_pipeline(message)

    # return result[0]["label"]


def predict_priority(message: str):

    keywords = [
        "urgent",
        "immediately",
        "asap",
        "critical",
        "failed"
    ]

    if any(
        word in message.lower()
        for word in keywords
    ):
        return "high"

    return "medium"


def generate_summary(message: str):
    return message[:50]

    # summary = summarizer(
    #     message,
    #     max_length=30,
    #     min_length=5,
    #     do_sample=False
    # )

    # return summary[0]["summary_text"]
    