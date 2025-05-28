import json
from fastapi.testclient import TestClient
from backend.server import app

# from ..backend.server import app

# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


client = TestClient(app)




def test_insert_order():
    # First insert a product 
    new_product = {
        "product_name": "Test Order Product",
        "uom_id": 1,
        "price_per_unit": 30
    }
    product_resp = client.post("/insertProduct", data={
        "data": json.dumps(new_product)
    })
    product_id = product_resp.json()["product_id"]

    new_order = {
        "customer_name": "John Doe",
        "grand_total": 60,
        "order_details": [
            {
                "product_id": product_id,
                "quantity": 2,
                "total_price": 60
            }
        ]
    }

    response = client.post("/insertOrder", data={
        "data": json.dumps(new_order)
    })

    assert response.status_code == 200
    data = response.json()
    assert "order_id" in data
    assert isinstance(data["order_id"], int)



def test_get_all_orders():
    response = client.get("/getAllOrders")
    assert response.status_code == 200
    orders = response.json()
    assert isinstance(orders, list)

    if orders:
        first_order = orders[0]
        assert "order_id" in first_order
        assert "customer_name" in first_order
        assert "total" in first_order
        assert "order_details" in first_order
        assert isinstance(first_order["order_details"], list)