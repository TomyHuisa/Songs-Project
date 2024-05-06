import sqlite3
import os 

import click
from flask import current_app, g

#constants with name and location of database
db_folder = current_app.instance_path
db_name = 'music.sqlite'
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()