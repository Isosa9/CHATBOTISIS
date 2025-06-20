import os
import mysql.connector
from dotenv import load_dotenv
from ia import consultar_ollama

load_dotenv()
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD","Sosaisis ")
DB_NAME = os.getenv("DB_NAME", "agrocomercial")

def fetch_products(query: str, limit: int = 5):
    sql = f"""
        SELECT nombre, categoria, descripcion, precio
          FROM productos
         WHERE nombre LIKE %s OR descripcion LIKE %s
         LIMIT %s;
    """
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cur = conn.cursor()
        q = f"%{query}%"
        cur.execute(sql, (q, q, limit))
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except mysql.connector.Error as e:
        print("❌ Error al conectar o consultar MySQL:", e)
        return []

