# Coding    :   UTF-8
# Team      :   Vincent
# Author    :   Vincent
# Created on:   2019/3/24 15:17
# File Name :   hello_flask.py
# Tool      :   PyCharm
from flask import Flask, request, jsonify, abort
import logging

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/users/', methods=['GET'])
def get_user_list():
    users = [
        {
            'first name': 'Bill',
            'last name': 'Gates'
        },
        {
            'first name': 'Steven',
            'last name': 'Jobs'
        },
        {
            'first name': 'Vincent',
            'last name': 'Huang'
        }
    ]
    return jsonify({'users': users})


@app.route('/users/<username>', methods=['GET'])
def show_user_profile(username):
    return 'User %s`s home page.' % username


@app.route('/users/login', methods=['POST'])
def login():
    if not request.json or 'username' not in request.json:
        abort(400)
    username = request.json['username']
    password = request.json['password']
    logging.info(username)
    logging.info(password)

    print('username:', username)
    print('password:', password)

    if username == 'rosydawn' and password == '123456':
        user = {
            'username': username,
            'password': password,
            'login': True
        }
    else:
        user = {
            'username': username,
            'password': password,
            'login': False
        }
    return jsonify({'login_info': user})


if __name__ == '__main__':
    app.run(debug=True)

