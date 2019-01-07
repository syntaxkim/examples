from functools import wraps

from flask import Flask, Blueprint, request
from flask_restplus import Api, Resource, fields
from marshmallow import Schema, fields as mar_fields, post_load, ValidationError

app = Flask(__name__)
# /api/doc to use Swagger UI
blueprint = Blueprint('api', __name__, url_prefix='/api')
authorizations = {
    'apikey': {
        'type': 'apiKey', # K is capital.
        'in': 'header',
        'name': 'X-API-KEY'
    }
}
api = Api(blueprint, doc='/doc', authorizations=authorizations) # Add 'doc=False' to turn off Swagger UI

app.register_blueprint(blueprint)
app.config.SWAGGER_UI_JSONEDITOR = True # This option is invalid on the latest version.

# Define data model.
# language = api.model('Language', {'language': fields.String('The language.')}) # 'id': fields.Integer('ID')
language = api.model('Language', {'language': fields.String('The language'), 'framework': fields.String('The framework')})

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwagrs):
        token = None
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']
        if not token:
            return {'message': 'Token is missing.'}, 401 # No need to use jsonify as already using Flask.
        if token != 't0ken':
            return {'message': 'Token is invalid.'}, 401
        print(f'TOKEN: {token}')

        return f(*args, **kwagrs)
    return decorated

class Language(object): # In the way of marshmallow
    def __init__(self, language, framework):
        self.language = language
        self.framework = framework

    def __repr__(self):
        return f'{self.language} is the language. {self.framework} is the framwork.'

class LanguageSchema(Schema):
    language = mar_fields.String()
    framework = mar_fields.String()

    @post_load
    def create_language(self, data):
        return Language(**data)

languages = []
# python = {'language': 'Python', 'id': 1}
python = Language(language='Python', framework='Flask')
languages.append(python)

@api.route('/languages')
class Languages(Resource):

    # The Commented decorators are Flask-RESTPlus' built-in functions that are slated for removal.
    # With that being said, using marshmallow is recommended.

    #@api.marshal_with(language, envelope='languages')
    # An optional envelope keyword argument is specified to wrap the resulting output. (more of a convention)
    @api.doc(security='apikey')
    @token_required
    def get(self):
        schema = LanguageSchema(many=True) # many=True returns a list of objects.
        return schema.dump(languages)

    @api.expect(language) # This decorator cannot be replaced with marshmallow yet.
    def post(self):
        schema = LanguageSchema()
        new_language = schema.load(api.payload) # new_language is a dict.
        # new_language['id'] = len(languages) + 1
        languages.append(new_language.data)
        return {'result': 'Language added.'}, 201

if __name__ == "__main__":
    app.run(debug=True)