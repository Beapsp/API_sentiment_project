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


def lasfrases(phrase,lan):
    query = f"""
    SELECT phrases_name
    FROM schema.movies.phrases
    WHERE phrases_name = '{phrase}';
    """

    eldata = pd.read_sql_query(query,engine)
    
    if lan == "en":
        eldata["en"] = eldata.phrases_name.apply(traduce)
        eldata.drop(columns="phrases_name", inplace=True)
        return eldata.to_json(orient="records")
    
    else:
        return eldata.to_json(orient="records")