# __init__.py
from flask import Flask, request, jsonify

app = Flask(__name__)
     
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    print(username)
    return jsonify({'username': username, "password": password, 'email': email}), 200



@app.route('/register')
def register():
    data = request.args.get("username")





if __name__ == "__main__":
    app.run(debug=True)
