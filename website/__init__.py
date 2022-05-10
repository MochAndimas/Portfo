from flask import Flask


def cretae_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Rcd32011!'

    from .views import views
    from .contact import contact
    from .album import album

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(contact, url_prefix="/")
    app.register_blueprint(album, url_prefix="/")

    return app
