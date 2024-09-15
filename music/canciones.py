from flask import Blueprint,render_template
from . import db 
bp = Blueprint('tracks',__name__, url_prefix= '/tracks')

@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta = """
            SELECT name FROM tracks
            WHERE TrackId = ? ;
    """
    
    res = con.execute(consulta, (id,))
    tracks= res.fetchone()
    lista_canciones = res.fetchall()
    pagina = render_template('detalle_canciones.html', 
                            tracks=tracks,   
                            canciones=lista_canciones)
    return pagina

@bp.route('/')
def albums():
    data_base = db.get_db() #Consigue la base de datos que estaba en db.py#
    consultaPrincipal = """
            SELECT name, TrackId FROM tracks;
          """
    
    result = data_base.execute(consultaPrincipal)
    lista_de_tracks = result.fetchall()
    
    return render_template("canciones.html", canciones=lista_de_tracks)