from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = ""
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacao = request.form["operacao"]

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                resultado = num1 / num2 if num2 != 0 else "Erro: Divisão por zero"
            else:
                resultado = "Operação inválida"
        except ValueError:
            resultado = "Digite números válidos"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
