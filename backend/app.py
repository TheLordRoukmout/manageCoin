from flask import Flask, render_template, jsonify, request
#from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from scriptData import get_user_from_json
from logInScript import checkLog  # La fonction checkLog doit exister dans ce fichier
from apiConnect import responApiJson

app = Flask(__name__)
CORS(app)

#app.config["JWT_SECRET_KEY"] = "secret_key_here"  # Remplace par une vraie clé secrète
#jwt = JWTManager(app)

@app.route('/')
def home():
    return render_template("index.html")  # Page d'accueil

@app.route('/api/users', methods=['GET'])
#@jwt_required()  # Cette route est protégée par un token JWT
def get_data():
    #current_user = get_jwt_identity()  # Récupérer l'utilisateur connecté à partir du token JWT
    users = get_user_from_json()

    return jsonify(users)

@app.route('/api/coinlist', methods=['GET'])
def get_coinlist():
    coinlist = responApiJson()
    return jsonify(coinlist)

#Function et route à terminer
@app.route('/api/login', methods=['POST'])
def login():
    email = request.json.get("email", None)  # Récupérer l'email envoyé dans la requête
    password = request.json.get("password", None)  # Récupérer le mot de passe

    # Appel de la fonction checkLog avec les identifiants récupérés
    return checkLog(email, password)

if __name__ == "__main__":
    app.run(debug=True)
