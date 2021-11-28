import sqlalchemy as alch
import os
import dotenv

dotenv.load_dotenv()

passw = os.getenv("pass_sql") #incluir contraseña en .env
dbName = "schema_movies"
connectionData = f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(connectionData)