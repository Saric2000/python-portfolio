from typing import Any


from transformers import pipeline
import matplotlib.pyplot as plt

# 🔹 Kreiraj sentiment analizator (model iz HuggingFace)
analyzer = pipeline("sentiment-analysis")

# 🔹 Unesi više rečenica za analizu
texts = [
    "I love this product! It's amazing and works perfectly.",
    "This is the worst service I have ever used.",
    "It's okay, nothing special but not bad either.",
    "Absolutely fantastic experience!",
    "I'm disappointed, it didn't meet my expectations."
]

results = analyzer(texts)

for text, res in zip(texts, results):
    print(f"Text: {text}\nSentiment: {res['label']} ({float(res['score'])*100:.2f}%)\n")

labels = [res['label'] for res in results]
scores = [res['score'] for res in results]

colors = ["#4caf50" if l == "POSITIVE" else "#f44336" if l == "NEGATIVE" else "#9e9e9e" for l in labels]

plt.figure(figsize=(10, 5))
bars = plt.barh(range(len(texts)), scores, color=colors)
plt.yticks(range(len(texts)), [t[:40] + "..." for t in texts])
plt.xlabel("Confidence Score")
plt.title("AI Sentiment Analysis Results")

for i, (bar, label) in enumerate(zip(bars, labels)):
    plt.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2,
             label, va="center", fontsize=9, weight="bold")

plt.tight_layout()
plt.show()
