from flask import Flask, render_template

app = Flask(__name__)


# construct pagine of site

# route -> monitoramento.com/Temperatura
# funcao  -> o que será exibido
@app.route("/")
def homepage(valueTemperature):
    return render_template("index.html", valueTemp=80)

@app.route("/contato")
def contato():
    return "renan.saraiva@academico.ifpb.edu.br"

# run site
if __name__ == "__main__":
    app.run(debug=True)

app.run(debug=True)
