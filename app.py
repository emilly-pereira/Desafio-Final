from flask import Flask, jsonify, redirect
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

# JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# Swagger
SWAGGER_URL = '/swagger'
API_DOC_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_DOC_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/', methods=['GET'])
def index():
    return {"mensagem": "Ola, bem-vindo ao Desafio Final!"}, 200

@app.route('/docs', methods=['GET'])
def docs():
    return redirect('/swagger/')

@app.route('/items', methods=['GET'])
def get_items():
    items = [{"id": 1, "name": "item1"},
             {"id": 2, "name": "item2"},
             {"id": 3, "name": "item3"}]
    return jsonify(items=items), 200

@app.route('/login', methods=['POST'])
def login():
    access_token = create_access_token(identity="user")
    return jsonify(access_token=access_token), 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="Protected route"), 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 1313))
    app.run(host='0.0.0.0', port=port)
