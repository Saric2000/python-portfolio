from flask import Flask, jsonify
import random
import os
import csv

app = Flask(__name__)

# DEFAULT_QUOTES = [
#     "Code is like humor. When you have to explain it, it's bad.",
#     "Experience is the name everyone gives to their mistakes.",
#     "In order to be irreplaceable, one must always be different.",
#     "Talk is cheap. Show me the code.",
#     "First, solve the problem. Then, write the code."
# ]

def ensure_quotes_csv(csv_path: str) -> None:
    if os.path.exists(csv_path):
        return
    # Create CSV with a header and default quotes
    '''with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["quote"])  # header
        # Add some default quotes for new users
        default_quotes = [
            "Code is like humor. When you have to explain it, it's bad.",
            "Experience is the name everyone gives to their mistakes.",
            "In order to be irreplaceable, one must always be different.",
            "Talk is cheap. Show me the code.",
            "First, solve the problem. Then, write the code."
        ]
        for q in default_quotes:
            writer.writerow([q])'''

def load_quotes_from_csv(csv_path: str) -> list:
    quotes_list = []
    try:
        with open(csv_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                text = row.get("quote", "").strip()
                if text:
                    quotes_list.append(text)
    except Exception:
        quotes_list = []
    
    # Fallback to defaults if CSV is empty or malformed
    if not quotes_list:
        quotes_list = [
            "Code is like humor. When you have to explain it, it's bad.",
            "Experience is the name everyone gives to their mistakes.",
            "In order to be irreplaceable, one must always be different.",
            "Talk is cheap. Show me the code.",
            "First, solve the problem. Then, write the code."
        ]
    return quotes_list

# Ensure CSV exists and load quotes
CSV_FILE = "quotes.csv"
ensure_quotes_csv(CSV_FILE)
quotes = load_quotes_from_csv(CSV_FILE)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang=\"en\">
    <head>
        <meta charset=\"UTF-8\" />
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
        <title>Random Quote</title>
        <style>
            body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 40px; }
            .card { max-width: 640px; padding: 24px; border: 1px solid #e5e7eb; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
            button { background: #2563eb; color: white; border: 0; padding: 10px 16px; border-radius: 8px; cursor: pointer; }
            button:hover { background: #1e40af; }
            #quote { margin-top: 16px; font-size: 1.25rem; line-height: 1.6; }
        </style>
    </head>
    <body>
        <div class=\"card\">
            <h1>Random Quote</h1>
            <p>Press button under to get a random quote.</p>
            <button id=\"loadBtn\">Quote</button>
            <div id=\"quote\"></div>
        </div>
        <script>
            const btn = document.getElementById('loadBtn');
            const box = document.getElementById('quote');
            async function loadQuote() {
                box.textContent = 'Učitavam...';
                try {
                    const res = await fetch('/quote');
                    if (!res.ok) throw new Error('Greška ' + res.status);
                    const data = await res.json();
                    box.textContent = '"' + data.quote + '"';
                } catch (err) {
                    box.textContent = 'Došlo je do greške pri učitavanju citata.';
                }
            }
            btn.addEventListener('click', loadQuote);
        </script>
    </body>
    </html>
    """ 

@app.route("/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True)
