import os 
import sqlite3

import click
from flask import current_app, g 

#Constante con nombre y locación del database
db_folder = current_app.instance_path
db_name = 'Musicas.sqlite'
db_file = os.path.join(db_folder,db_name)
db_sql_file = 'datos.sql'

def dict_factory(cursor, row):
   """Arma un diccionario con los valores de la fila."""
   fields = [column[0] for column in cursor.description]
   return {key: value for key, value in zip(fields, row)}

def get_db():
    if 'db' not in g: 
        g.db = sqlite3.connect(
            db_file,
            detect_types=sqlite3.PARSE_COLNAMES
        )
        g.db.row_factory = sqlite3.Row
    
    return g.db

def close_db(e=None):
    db= g.pop('db',None)


    if db is not None:
        db.close()

def init_db():
    #Asegurar si la instancia de la carpeta existe.
    try: 
        os.makedirs(db_folder)
    except OSError:
        pass
    db = get_db()
    with current_app.open_resource(db_sql_file) as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Limpia la data existente y crea una nueva."""
    init_db()
    click.echo('Inicializa la base de datos')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)