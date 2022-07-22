#__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET KEY"] = 'kiki'

    #app에 다른 곳에 있는 BP가져오기
    from.views import views
    from.auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)
    return app

