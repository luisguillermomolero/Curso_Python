import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv()

def crear_base_de_datos(nombre, usuario, password, host="localhost"):
    try:
        con = psycopg2.connect(
            dbname="postgres",
            user=usuario,
            password=password,
            host=host,
            client_encoding='utf8'
        )
        
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (nombre,))
        if not cur.fetchone():
            cur.execute(
                sql.SQL("CREAT DATABASE {} ENCODING 'UTF8").format(sql.Identifier(nombre))
            )
            print(f"Base de datos '{nombre}' creada satisfactoriamente")
        else:
            print(f"La base de datos '{nombre}' ya existe.")
    except Exception as e:
        print("ERROR en la cración de la bas de datos", e)
    finally:
        if 'cur' in locals(): cur.close()
        if 'con' in locals(): con.close()

if __name__ == "__main__":
    crear_base_de_datos(
        os.getenv("DB_USER", "postgres"),
        os.getenv("DB_PASSWORD", "1126254560"),
        os.getenv("DB_HOST", "localhost"),
        os.getenv("DB_NAME", "tarea_db")
    )