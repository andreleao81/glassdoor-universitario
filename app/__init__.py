from flask import Flask, request, jsonify, render_template
from .extensions import db, migrate, ma, cors
from .config import Config
from .controllers.UserController import user_api
from .controllers.CollegeClassController import college_class_api
from .controllers.ProfessorController import professor_api
from .controllers.ProfessorEvaluationController import professor_evaluation_api
from .controllers. ClassEvaluationController import college_class_evaluation_api

from flasgger import Swagger
from flask_swagger_ui import get_swaggerui_blueprint
import yaml
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
    app.register_blueprint(professor_evaluation_api)
    app.register_blueprint(college_class_evaluation_api)

    

   # swagger = Swagger(app)
    # swagger = Swagger(app, template={
    #     "info": {  
    #         "title": "Flask API",
    #         "description": "This is a simple Flask API",
    #         "version": "1.0.0"
    #     }
    # })

    @app.route('/swagger')
    def get_docs():
        return render_template('swaggerui.html')

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/add_one/<int:number>')

    def add_one(number):
        """
        Add one to a number
        ---
        parameters:
          - name: number
            in: path
            type: integer
            required: true
        responses:
          200:
            description: The input number plus one
        """
        return {'result': number + 1}   
    
    @app.route('/api')
    def get_api():
        hello_dict = {'en': 'Hello', 'es': 'Hola', 'pt-br': 'Ahola'}
        lang = request.args.get('lang')
        return jsonify(hello_dict[lang])

   
    # with app.app_context():
    #     for rule in app.url_map.iter_rules():
    #         endpoint = app.view_functions[rule.endpoint]
    #         operations = {}
    #         docstring = endpoint.__doc__
    #         if docstring:
    #             for line in docstring.strip().split('\n'):
    #                 line = line.strip()
    #                 if line.startswith('- '):
    #                     operation = yaml.safe_load(line[2:])
    #                     if operation:
    #                         operations.update(operation)
    #         spec.path(
    #             rule=rule.rule,
    #             view=endpoint,
    #             operations=operations,
    #         )

    #     with open('app/static/swagger.json', 'w') as f:
    #         dict_ = yaml.load(io.StringIO(spec.to_yaml()), Loader=yaml.SafeLoader)
    #         dict_['security'] = [{'BearerAuth': []}]
    #         with open('app/static/swagger.json', 'w') as f:
    #             json.dump(dict_, f)

    #     SWAGGER_URL = '/api/docs'  
    #     API_URL = '/static/swagger.json'  
    
    # swaggerui_blueprint = get_swaggerui_blueprint(
    #     SWAGGER_URL,
    #     API_URL,
    #     config={
    #         'app_name': ""
    #     }
    # )

    # app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    return app