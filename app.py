from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/Home.html")
def inicio():
    return render_template("Home.html")

@app.route("/Quem_Sou.html")
def sobre():
    return render_template("Quem_Sou.html")

@app.route("/Projetos.html")
def projetos():
    return render_template("Projetos.html")



