import pandas as pd
from config.configuration import engine

def sustituye(x):

    """
    Esta función me sustituye los apóstrofos de los elementos de mi dataframe
    por comillas de lado para que no se confundan con comillas
    
    """
    x = str(x).replace('"', "`")
    x = str(x).replace("'", "`")
    return x


def dameId(lista,string):
    """
    Esta función devuelve el ID de lo que le pidamos sabiendo que ese elemento EXISTE
    """
    if lista == "movie":
        return list(engine.execute(f"SELECT IDMovie FROM movie WHERE movie_name ='{string}';"))[0][0]
    elif lista == "context":
        return list(engine.execute(f"SELECT IDContext FROM context WHERE context_name ='{string}';"))[0][0]


peli_id=[]
for m in movies3:
    id_movie= list((cl.dameId("movie", m),m))
    peli_id.append(id_movie)

def replace_movie_id(x):
    """
    Esta función itera por la lista de Películas+ID para que cada vez que encuentre una película
    me devuelva el ID
    
    """
    for mov in range(len(peli_id)):
        if x == (peli_id[mov][1]):
            return peli_id[mov][0]

contexto_id=[]
for c in list(df_movies.Context.unique()):
    id_context = list((cl.dameId("context", c),c))
    contexto_id.append(id_context)
    
def replace_context_id(y):
    """
    Esta función itera por la lista de Contexto+ID para que cada vez que encuentre el contexto de una película
    me devuelva el ID
    
    """
    for cont in range(len(contexto_id)):
        if y == (contexto_id[cont][1]):
            return contexto_id[cont][0]