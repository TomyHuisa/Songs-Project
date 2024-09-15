from flask import Blueprint,render_template
from . import db 
bp = Blueprint('artist',__name__, url_prefix= '/artist')

@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 = """
        SELECT name FROM artists WHERE ArtistId = ?;
    """
    consulta2 = """
        SELECT AlbumId ,Title FROM albums WHERE ArtistId = ?;
    """
    
    res = con.execute(consulta1, (id,))
    artista = res.fetchone()
    res = con.execute(consulta2, (id,))
    lista_artist= res.fetchall()
    pagina = render_template('detalle_artist.html', 
                            artista=artista,   
                            artists=lista_artist)
    return pagina

@bp.route('/')
def artists():
    data_base = db.get_db() #Consigue la base de datos que estaba en db.py#
    ask = """
            SELECT name, ArtistId FROM artists
            ORDER BY name ASC;
          """
    
    result = data_base.execute(ask)
    lista_de_artist = result.fetchall()
    
    return render_template("artists.html", artists=lista_de_artist)
