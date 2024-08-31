# app.py
from flask import Flask

from router.base_route import base_bp
from router.chat_route import chat_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(base_bp, url_prefix='/base')
    app.register_blueprint(chat_bp, url_prefix='/chat')


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
