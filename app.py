from flask import Flask, render_template
from produtos import produtos

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html", produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True)