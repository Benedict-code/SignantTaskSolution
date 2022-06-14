import base64
import json
import os
import tempfile

import pytest

from Flasky.demo_app import create_app
from Flasky.demo_app.db import init_db

Registration_data = {
    "username":"usernamee",
    "password":"password",
    "firstname":"firstnamee",
    "lastname":"lastname",
    "mobile":"+35800000000"
}

@pytest.fixture
def client():
    # Temporal file
    db_fd, db_path = tempfile.mkstemp()
    app = create_app(
        {
            "TESTING": True,
            "DATABASE": db_path
        }
    )
    #test client
    with app.test_client() as client:
        with app.app_context():
            init_db()
            yield client

    #unneeded resource
    os.close(db_fd)
    os.unlink(db_path)

def setUp(client):
    #iterate for every test
    header = {
        "Content-Type":"application/json"
    }
    user_endpoint = "/app/users"

    #post request
    response = client.post(user_endpoint, json=Registration_data, headers=header)
    assert response.status_code == 201

def get_auth(client, username, password):
    auth_string = "{}:{}".format(username,password)
    credentials = base64.b64encode(f"{auth_string}".encode()).decode("utf-8")
    token_endpoint = "/api/auth/token"

    #header with BASIC authentication
    header = {
        "Authorization":f"Basic{credentials}",
        "Content-Type":"application/json"
    }
    #extract token by GET request
    response = client.get(token_endpoint, headers=header)
    assert response.status_code == 200
    data=json.loads(response.data)
    token = data["token"]
    return token

def test_add_user(client):
    header = {
        "Content-Type":"application/json"
    }
    user_endpoint = "/api/users"
    #post request
    response = client.post(user_endpoint, json=Registration_data, headers=header)
    assert response.status_code == 201
    setUp(client)

def test_get_review_users(client):
    setUp(client)
    username = Registration_data["username"]
    password = Registration_data["password"]
    user_endpoint = "/app/users"
    token = get_auth(client, username, password)
    header = {
        "Token":f"{token}",
        "Content-Type":"application/json"
    }

    response = client.get(user_endpoint, headers=header)
    assert response.status_code == 200
    #payload response
    assert b'payload' in response.data
    data = json.loads(response.data)
    #payload data
    assert len(data['payload']) == 1
    assert data['payload'][0] == username

def test_get_user_info(client):
    setUp(client)
    username = Registration_data["username"]
    password = Registration_data["password"]
    username_endpoint = f"/api/users/{username}"

    token = get_auth(client, username, password)
    header = {
        "Token":f"{token}",
        "Content-Type":"application/json"
    }

    response = client.get(username_endpoint, headers=header)
    assert response.status_code == 200

def test_update_put_user_info(client):
    setUp(client)
    username = Registration_data["username"]
    password = Registration_data["password"]
    username_endpoint = f"/api/users/{username}"

    token = get_auth(client, username, password)
    header = {
        "Token":"{token}",
        "Content-Type":"application/json"
    }
    response = client.put(username_endpoint, json=dict(firstname="firstnamee"), headers=header)
    assert response.status_code == 201
