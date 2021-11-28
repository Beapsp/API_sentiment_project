from flask import Flask, request
from flask import jsonify
import src.sql_tools as sqt

app = Flask(__name__)

@app.route("/movies") #endpoints para conseguir el nombre de las películas
def dame_movies():
    movies = sqt.peliculas() #función de sql_tools para la query
    return jsonify(movies)


@app.route("/phrases") #endpoints para conseguir el nombre de las películas
def dame_phrases():
    phrases = sqt.frases() #función de sql_tools para la query
    return jsonify(phrases)


@app.route("/context") #endpoints para conseguir el nombre de las películas
def dame_context():
    context = sqt.contexto() #función de sql_tools para la query
    return jsonify(context)




@app.route("/phrases/<name>")
def frases(name):
    idioma = request.args.get("idioma")
    frasecitas = sqt.lasfrases(name, idioma)
    return jsonify(frasecitas)






app.run(debug=True) #runnea todo el rato