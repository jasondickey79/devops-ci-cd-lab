from flask import Flask, request, jsonify
import uuid
import logging

app = Flask(__name__)
logging.bsicConfig(level=logging.INFO)

@app.route("/process-order", methods=["POST"])
def process_order():
    data = request.json
    order_id = str(uuid.uuid4())
    
    logging.info(f"Processing order: {data}")
    
    return jsonify({
        "status": "processed"
        "order_id": order_id
    }), 200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
