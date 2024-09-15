from flask import Blueprint,render_template
from . import db 
bp = Blueprint('albums',__name__, url_prefix= '/albums')

@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 = """
        SELECT Title FROM albums WHERE AlbumId = ?;
    """
    consulta2 = """
        SELECT t.name, t.TrackId FROM albums a
        JOIN tracks t ON a.AlbumId = t.AlbumId
        WHERE a.AlbumId = ?; 
    """
    
    res = con.execute(consulta1, (id,))
    albums = res.fetchone()
    res = con.execute(consulta2, (id,))
    lista_canciones = res.fetchall()
    pagina = render_template('detalle_albums.html', 
                            albums=albums,   
                            canciones=lista_canciones)
    return pagina

@bp.route('/')
def albums():
    data_base = db.get_db() #Consigue la base de datos que estaba en db.py#
    consultaPrincipal = """
            SELECT Title,AlbumId FROM albums
            ORDER BY Title ASC;
          """
    
    result = data_base.execute(consultaPrincipal)
    lista_de_albums = result.fetchall()
    
    return render_template("albums.html", albums=lista_de_albums)
