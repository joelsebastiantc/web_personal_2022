from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/") #indica que será la página de inicio
def inicio():
    return render_template("index.html")

@app.route("/map-dataset") #indica que será la página de inicio
def map():
    return render_template("coddi_map.html")
