from flask import Blueprint, render_template
from . import db

bp = Blueprint('artist', __name__, url_prefix='/artist')
@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 = """
                    SELECT Name FROM artists
                    WHERE ArtistId = ?;
                """
    consulta2 = """
                    SELECT a.Title FROM albums a
                    JOIN artists ar ON ar.ArtistId = a.ArtistId
                    WHERE a.ArtistId = ?;
                """
    
    res = con.execute(consulta1, (id,))
    artist = res.fetchone()
    res = con.execute(consulta2, (id,))
    albumlist = res.fetchall()
    pagina = render_template('detail_artist.html',
                            artist=artist,
                            albums=albumlist)
    return pagina