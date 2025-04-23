from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():

        from app.views.views_pages import views_pages
        app.register_blueprint(views_pages)

    return app