import os
import socket
from unittest.mock import patch
from app import app

# Test the Flask routes and Redis connection

def test_hello_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_hello_content():
    client = app.test_client()
    response = client.get('/')
    assert b'Bonjour youtube!' in response.data

'''def test_redis_connection():
    with patch('app.redis.incr') as mock_incr:
        mock_incr.return_value = 1
        visites = app.redis.incr("compteur")
        assert visites == 1
'''
def test_custom_nom():
    os.environ['NOM'] = 'custom_name'
    client = app.test_client()
    response = client.get('/')
    assert b'Bonjour custom_name!' in response.data
