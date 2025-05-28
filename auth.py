from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

# Instâncias globais
db = SQLAlchemy()
jwt = JWTManager()
auth_bp = Blueprint('auth', __name__)

# Modelo de usuário
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  

# Rota de registro
@auth_bp.route('/register', methods=['POST'])
def register_users():
    """
    Registro de novo usuário.
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      201:
        description: Usuário criado com sucesso
      400:
        description: Erro de entrada ou usuário já existe
    """
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Dados inválidos"}), 400

    if Users.query.filter_by(username=data['username']).first():
        return jsonify({"error": "Usuário já existe"}), 400

    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = Users(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "Usuário criado com sucesso"}), 201

# Rota de login
@auth_bp.route('/login', methods=['POST'])
def login_user():
    """
    Login do usuário. Retorna um token JWT.
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: Login bem-sucedido, retorna token JWT
      401:
        description: Credenciais inválidas
    """
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Dados inválidos"}), 400

    user = Users.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        token = create_access_token(identity=str(user.id))  
        return jsonify({"access_token": token}), 200

    return jsonify({"error": "Credenciais inválidas"}), 401

# Rota de verificação de token 
@auth_bp.route('/verifytoken', methods=['GET'])
@jwt_required()
def verify_token():
    current_user_id = get_jwt_identity()
    return jsonify({"msg": "Token válido", "user_id": current_user_id}), 200
