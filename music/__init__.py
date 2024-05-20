from flask import Flask, send_file, render_template


app = Flask(__name__)
#
with app.app_context():
    from . import db
    db.init_app(app)

@app.route('/themes')
def songs():
    data_base = db.get_db() #Consigue la base de datos que estaba en db.py#
    ask = """
            SELECT Name FROM artists
            ORDER BY Name ASC;
          """
    
    result = data_base.execute(ask)
    list_of_result = result.fetchall()
    pagina = render_template("songs.html", ask=list_of_result)
    
    return pagina


from . import db
db.init_app(app)

    