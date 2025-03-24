from flask import Flask, request, render_template_string

app = Flask(__name__)

saved_text = ""  # Variabel för att lagra texten

@app.route("/", methods=["GET", "POST"])
def home():
    global saved_text
    if request.method == "POST":
        saved_text = request.form.get("text_input")  # Hämta texten från formuläret
    return render_template_string('''
        <form method="POST">
            <input type="text" name="text_input" placeholder="Skriv något här" required>
            <button type="submit">Spara</button>
        </form>
        <p>Senast sparade text: {{ saved_text }}</p>
    ''', saved_text=saved_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

