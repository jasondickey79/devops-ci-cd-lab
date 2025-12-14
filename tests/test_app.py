from app.app import app

def test_process_order():
    client = app.test_client()
    response = client.post(
        "/process-order",
        json={"item": "widget", "quantity": 2}
    )
    assert response.status_code == 200
    assert "order_id" in response.json
    
