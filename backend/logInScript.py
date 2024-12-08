from flask_jwt_extended import create_access_token
from scriptData import get_user_from_json
from flask import jsonify

def checkLog(email, password):
    # Récupérer les utilisateurs depuis le fichier JSON
    users = get_user_from_json()

    # Vérifier les identifiants
    for user in users:
        if user["email"] == email and user["password"] == password:
            # Si les identifiants sont valides, créer un token JWT
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token), 200

    # Si aucun utilisateur ne correspond, renvoyer une erreur 401
    return jsonify({"msg": "Identifiants invalides"}), 401
