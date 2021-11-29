# Proyecto_crear_API
![imagen](imagen.png)

## OBJETIVO: 
El objectivo de este proyecto es crear un API que me permita obtener información de una base de datos referente a nombres de películas, frases célebres de estas y el contexto en el que fueron dichas. Además haré un análisis de sentimientos de dichas frases mediante NLP.

## EJECUCIÓN:
En primer lugar importo el csv con la información de películas, y limpio el dataframe para poder insertar los datos en MySQL. La estructura de mis datos en las tablas de la base de datos es la siguiente:
![imagen](diagrama.jpg)
A partir de estos datos voy a crear los endpoints de la API tanto para silicitar información como para insertar.

## FUNCIONAMIENTO API:
Iré añadiendo endpoints a las siguiente url : http://127.0.0.1:5000/

### --> LLAMADAS TIPO GET
 - movie

 Este endpoint me devuelve el nombre de las películas  
 ```
 movies = requests.get("http://127.0.0.1:5000/movies").json()
```
 - phrases

 Este endpoint me devuelve las frases de las películas  
 ```
 phrases = requests.get("http://127.0.0.1:5000/phrases").json()
```
 
 - context

 Este endpoint me devuelve los contextos en los que fueron dichos las frases de las películas  
 ```
 context = requests.get("http://127.0.0.1:5000/context").json()
```

 - phrases/movies

 Este endpoint me devuelve frases de películas concretas que yo le pida también como endpoints  
 ```
 phrases2 = requests.get(f"http://127.0.0.1:5000/phrases/{movie}").json()
```

 - context/movies

 Este endpoint me devuelve los contextos en los que se dijeron las frases de películas concretas que yo le pida también como endpoints  
 ```
context2 = requests.get(f"http://127.0.0.1:5000/context/{movie}").json()  
```

 - complet

 Este endpoint me devuelve las frases y los contextos en los que se dijeron las frases de películas concretas que yo le pida también como endpoints  
 ```
completo = requests.get(f"http://127.0.0.1:5000/completo/{movie}").json()  
```

- traductor

 Este endpoint me devuelve las frases traducidas al español de las películas concretas que yo le pida también como endpoints  
 ```
traducción = requests.get(f"http://127.0.0.1:5000/frases_lan/{movie}?idioma=en").json()   
```

### --> LLAMADAS TIPO POST

- insert_phrase

 Este endpoint me incluye una frase de una película concreta, teniendo en cuenta tanto el ID de movies como el de context.  
 ```
requests.post("http://127.0.0.1:5000/nuevafrase", data= insert_phrase)  
```

- insert_movie

 Este endpoint me incluye una película en la tabla de películas con su ID. 
 ```
requests.post("http://127.0.0.1:5000/nuevamovie", data= insert_movie)  
```

### --> ANÁLISIS DE SENTIMIENTOS

- insert_movie

 Este endpoint me da la media de análisis de sentimientos respecto a la polaridad de las frases de la película que le incluya como en endpoint. 
 ```
requests.get(f"http://127.0.0.1:5000/sentimientos/{movie}") 
```
