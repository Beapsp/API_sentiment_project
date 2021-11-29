from flask import Flask, request
from flask import jsonify
import src.sql_tools as sqt

app = Flask(__name__)

@app.route("/movies") #endpoints para conseguir el nombre de las películas
def dame_movies():
    movies = sqt.peliculas() #función de sql_tools para la query
    return jsonify(movies)


@app.route("/phrases") #endpoints para conseguir las frases de las películas
def dame_phrases():
    phrases = sqt.frases() 
    return jsonify(phrases)


@app.route("/context") #endpoints para conseguir los contextos de las películas
def dame_context():
    context = sqt.contexto() 
    return jsonify(context)



@app.route("/phrases/<name>") #endpoints para conseguir las frases de películas concretas que yo le pida
def frases(name):
    frase_peli = sqt.lasfrases(name)
    return jsonify(frase_peli)


@app.route("/context/<name>") #endpoints para conseguir los contextos de películas concretas que yo le pida
def contexto(name):
    contexto_peli = sqt.loscontextos(name)
    return jsonify(contexto_peli)

@app.route("/completo/<movie>") #endpoints para conseguir los contextos de películas concretas que yo le pida
def complet(movie):
    todo_peli = sqt.completo(movie)
    return jsonify(todo_peli)



@app.route("/frases_lan/<movies>") 
def lasfrases_idioma(movie):
    lan = request.args.get("idioma")
    ran = sqt.traduccion(lan, movie)
    return jsonify(ran)




@app.route("/nuevafrase", methods=["POST"])
def insertafrase():
    pelicula = request.form.get("movie")
    contexto = request.form.get("context")
    frase = request.form.get("phrases")
    return sqt.nuevafrase(pelicula, contexto, frase)




app.run(debug=True) #runnea todo el rato