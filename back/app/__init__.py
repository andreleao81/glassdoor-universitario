from flask import Flask



def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, World!'
   

   
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