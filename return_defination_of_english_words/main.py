from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def api(word):
    defination = word.upper()
    result = {
        "defination":defination,
        "word":word
    }
    return result

if __name__ == "__main__":
    app.run(debug=True)