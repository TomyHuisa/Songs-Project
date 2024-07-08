from flask import Blueprint, redirect, render_template, request, url_for
from . import db

consulta = """

            SELECT Name FROM artists

           """

res = con.execute(consulta, (id,))
artist = res.fetchall()
pagina = render_template('songs.html',
                        artists=artist)

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

@bp.route('/new', methods=('GET', 'POST'))
def nuevo():
    if request.method == 'POST':
        Name = request.form['Name']
        
        con = db.get_db()
        consulta = """
                    INSERT INTO artist(Name)
                    VALUES (?);
                   """
        con.execute(consulta, (Name))
        con.commit()
        return redirect(url_for('artist.artist'))
    else:
        pagina = render_template('new_artist.html')
        return pagina