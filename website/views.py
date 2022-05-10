from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/<string:page_name>")
def html_route(page_name):
    return render_template(page_name)
