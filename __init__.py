from flask import Flask, render_template


app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/themes')
def songs():
    data_base = db.get_db()
    ask = """
            
          """
    
    result = data_base.execute(ask)
    list_of_result = result.fetchall()
    
    return render_template("songs.html", songs=list_of_result) 