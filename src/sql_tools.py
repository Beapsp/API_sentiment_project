from config.configuration import engine
import pandas as pd
from textblob import TextBlob
from googletrans import Translator
import re
import spacy
import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer



def peliculas():
    query = list(engine.execute("SELECT distinct(movie_name) FROM schema_movies.movie;"))
    lista =  [{"movie": elemento[0]} for elemento in query]
    return lista


def frases():
    query = list(engine.execute("SELECT distinct(phrases_name) FROM schema_movies.phrases;"))
    lista =  [{"phrase": elemento[0]} for elemento in query]
    return lista


def contexto():
    query = list(engine.execute("SELECT distinct(context_name) FROM schema_movies.context;"))
    lista =  [{"context": elemento[0]} for elemento in query]
    return lista


def lasfrases(movie):
    query = pd.read_sql_query(f"""
    SELECT phrases.phrases_name, movie.movie_name 
    FROM phrases
    INNER JOIN movie
    ON movie.IDMovie=phrases.Movie_IDMovie
    WHERE movie_name = '{movie}';
    """,engine).to_json(orient="records")
    return query


def loscontextos(contexto):
#me convierte en df la tabla de SQL, porque estoy metiendo los dos elementos en el SELECT
    query = pd.read_sql_query(f"""
    SELECT context.context_name, movie.movie_name 
    FROM context
    INNER JOIN movie
    ON movie.IDMovie=context.Movie_IDMovie
    WHERE movie_name = '{contexto}';
    """,engine).to_json(orient="records") #ME SALDRÁ LISTA DE DICCIONARIOS, EL NOMBRE DE LA COLUMNA ES LA KEY Y LO DE DENTRO ES ELVALUE.
    return query


def completo(todo):

    query = pd.read_sql_query(f"""
    SELECT context.context_name, movie.movie_name, phrases.phrases_name
    FROM phrases
    INNER JOIN movie
    ON movie.IDMovie=phrases.Movie_IDMovie
    INNER JOIN context
    ON context.IDContext=phrases.Context_IDContext
    WHERE movie_name = '{todo}';
    """,engine).to_json(orient="records") #ME SALDRÁ LISTA DE DICCIONARIOS, EL NOMBRE DE LA COLUMNA ES LA KEY Y LO DE DENTRO ES ELVALUE.
    return query



def traduccion(lang, movie):
    trans = Translator()
    if lang == "es":
        return lasfrases(movie)
    elif lang == "en":
        notraduci = lasfrases(movie)
        traducido = trans.translate(lasfrases(movie), dest="es").text
        return f" Traducción: {traducido}"
    else:
        return lasfrases(movie)



def nuevafrase(phrases, context, movie):

    engine.execute(f"""
    INSERT INTO phrases (phrases_name, Context_IDContext, Movie_IDMovie)
    VALUES ('{phrases}', {context}, {movie});
    """)
    
    return f"Se ha introducido correctamente: {phrases} {context} {movie}"


def nuevapeli(movie):

    engine.execute(f"""
    INSERT INTO movie(movie_name)
    VALUES ('{movie}');
    """)
    return f"Se ha introducido correctamente: {movie}"


def analisis_sentimientos(movie):
    query = pd.read_sql_query(f"""
    SELECT phrases.phrases_name
    FROM phrases
    INNER JOIN movie
    ON movie.IDMovie=phrases.Movie_IDMovie
    WHERE movie_name = '{movie}'; 
    """,engine) #quiero un df, por eso retiro el .json y el record
    return query
    

def tokenizer(phrases):
    nlp = spacy.load("en_core_web_sm")
    tokens = nlp(phrases)
    filtradas = []
    for token in tokens: #saco las palabras importantes para el análisis de sentimientos
        if not token.is_stop:
            lemma = token.lemma_.lower().strip()
            if re.search('^[a-zA-Z]+$',lemma): # Esto me quita las interrogaciones
                filtradas.append(lemma)
    return " ".join(filtradas)


def sentiment(phrases):
    sia = SentimentIntensityAnalyzer()
    polaridad = sia.polarity_scores(phrases)
    pol = polaridad["compound"]
    return pol

