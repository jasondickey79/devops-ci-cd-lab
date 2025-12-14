import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.app import app

def test_process_order():
    client = app.test_client()
    response = client.post(
        "/process-order",
        json={"item": "widget", "quantity": 2}
    )
    assert response.status_code == 200
    assert "order_id" in response.json
    
