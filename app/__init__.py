from flask import Flask, request, jsonify, render_template
from .extensions import db, migrate, ma, cors
from .config import Config
from .controllers.UserController import user_api
from .controllers.CollegeClassController import college_class_api
from .controllers.ProfessorController import professor_api

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    cors.init_app(app, resources={r"/*":{"origins":"*"}})

    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    #blueprints
    app.register_blueprint(user_api)
    app.register_blueprint(college_class_api)
    app.register_blueprint(professor_api)

    @app.route('/swagger')
    def get_docs():
        return render_template('swaggerui.html')

    return app