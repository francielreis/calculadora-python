from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = ""

    if request.method == "POST":
        expressao = request.form["expressao"]
        try:
            resultado = eval(expressao)
        except:
            resultado = "Erro"

    return render_template("index.html", resultado=resultado)

app.run(host="0.0.0.0", port=5000)
