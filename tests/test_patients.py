from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_get_all_patients():
    response = client.get('/patients')
    assert response.status_code == 200
    # assert response.json()
