from flask import Blueprint, render_template

album = Blueprint("album", __name__)


@album.route("/")
def album_page():
    return render_template("album.html")
