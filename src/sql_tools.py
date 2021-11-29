from config.configuration import engine
import pandas as pd
from textblob import TextBlob
from googletrans import Translator



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
    if lang == "en":
        return lasfrases(movie)
    elif lang == "es":
        notraduci = lasfrases(movie)
        traducido = trans.translate(lasfrases(movie), dest="en").text
        return f" Traducción: {traducido}"
    else:
        return lasfrases(movie)



def nuevafrase(movie, context, phrases):

    engine.execute(f"""
    INSERT INTO phrases (Movie_IDMovie, Context_IDContext, phrases_name)
    VALUES ({movie}, '{context}', '{phrases}');
    """)
    
    return f"Se ha introducido correctamente: {movie} {context} {phrases}"

    

    #def random_aut_gen_2(lang, genero, autor):
    trans = Translator()
    if lang == "en":
        return random_aut_gen(genero, autor)
    elif lang == "es":
        sintraducir = random_aut_gen(genero, autor)
        traducido = trans.translate(random_aut_gen(genero,autor), dest="es").text
        return f"Traducción: {traducido}"
    else:
        return random_aut_gen(genero, autor)