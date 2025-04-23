import psycopg2

from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL") 
SECRET_KEY = os.getenv("SECRET_KEY")     

db_host = DATABASE_URL
db_port = "5432"  
db_user = "postgres"  
db_password = SECRET_KEY
connect_db = "trivia_db"

print(f"🔄 Intentando conectar a PostgreSQL en {db_host}:{db_port} como usuario '{db_user}'...")

try:

    with psycopg2.connect(
        dbname=connect_db,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    ) as connection:
        
        connection.autocommit = True
        print(f"✅ Conectado a la base de datos '{connect_db}'.")

        with connection.cursor() as cursor:
            print("🔍 Obteniendo lista de bases de datos...")


            list_databases_query = "SELECT datname FROM pg_database;"
            cursor.execute(list_databases_query)

          
            database_list = cursor.fetchall()

            if database_list:
                print("\n--- Bases de Datos Encontradas ---")
                for db in database_list:

                    print(f"- {db[0]}")
                print("----------------------------------")
                print(f"\n✅ Operación completada. {len(database_list)} bases de datos listadas.")
            else:

                print("🤔 No se encontraron bases de datos.")


except psycopg2.OperationalError as e:
    print("\n❌ Error de Conexión a PostgreSQL:")
    print(f"   {e}")
    print("\n   Por favor, verifica:")
    print(f"   1. Que el servidor PostgreSQL esté corriendo en '{db_host}:{db_port}'.")
    print(f"   2. Que el nombre de usuario ('{db_user}') y la contraseña sean correctos.")
    print(f"   3. Que el host ('{db_host}') sea accesible desde donde ejecutas el script.")
    print(f"   4. Que la base de datos de conexión ('{connect_db}') exista (generalmente 'postgres' sí existe).")
    print(f"   5. Que no haya un firewall bloqueando la conexión al puerto {db_port}.")


except Exception as e:
    print(f"\n❌ Ocurrió un error inesperado: {e}")

finally:
    print("\n🏁 Script finalizado.")