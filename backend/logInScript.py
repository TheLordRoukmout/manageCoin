from flask_jwt_extended import create_access_token
from scriptData import get_user_from_json
from flask import jsonify

def checkLog(email, password):
    users = get_user_from_json()

    # Vérifier les identifiants
    for user in users:
        if user["email"] == email and user["password"] == password:
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Identifiants invalides"}), 401
