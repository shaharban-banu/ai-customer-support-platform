from fastapi.testclient import TestClient

from app.main import app

client=TestClient(app)

def test_home():
    response=client.get('/')
    assert response.status_code==200

def test_ticket_api():
    response=client.post('/ticket',json={'message':'payment failed urgently'})
    assert response.status_code==200
    data=response.json()
    assert "category" in data
    assert "sentiment" in data
    assert "priority" in data
    assert "summary" in data

def test_get_tickets():
    response=client.get('/tickets')
    assert response.status_code==200