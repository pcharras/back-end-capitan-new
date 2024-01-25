from flask import Blueprint, request, jsonify, make_response,current_app
from werkzeug.security import generate_password_hash, check_password_hash
#from ..models import User
import jwt
import datetime
import uuid

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():

    auth = request.authorization

    print(auth)
    # if not auth or not auth.username or not auth.password:
    #     return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    # user = User.query.filter_by(username=auth.username).first()

    # if not user:
    #     return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    # if check_password_hash(user.password, auth.password):
    #     token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, current_app.config['SECRET_KEY'])

    #     return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    print("entro en signup")
    hashed_password = generate_password_hash(data['password'])
    #new_user = User(public_id=str(uuid.uuid4()), username=data['username'], password=hashed_password)
    #db.session.add(new_user)
    #db.session.commit()

    return jsonify({'message': 'Registered successfully'}), 201
