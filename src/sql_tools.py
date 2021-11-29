from config.configuration import engine
import pandas as pd
from textblob import TextBlob

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
#me convierte en df la tabla de SQL, porque estoy metiendo los dos elementos en el SELECT
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




def lasfrases(personaje,lan):
    query = f"""
    SELECT dialogue 
    FROM HP.frases 
    WHERE character_name = '{personaje}';
    """

    eldata = pd.read_sql_query(query,engine)
    
    if lan == "es":
        eldata["es"] = eldata.dialogue.apply(traduce)
        eldata.drop(columns="dialogue", inplace=True)
        return eldata.to_json(orient="records")
    elif lan == "en":
        return eldata.to_json(orient="records")
    
    else:
        return eldata.to_json(orient="records")



    #eldata = pd.read_sql_query(query,engine) 
    if lan == "en":
        eldata["en"] = eldata.phrases_name.apply(traduce)
        eldata.drop(columns="phrases_name", inplace=True)
        return eldata.to_json(orient="records") #ME SALDRÁ LISTA DE DICCIONARIOS, EL NOMBRE DE LA COLUMNA ES LA KEY Y LO DE DENTRO ES ELVALUE.
    
    else:
        return eldata.to_json(orient="records")