from flask import Flask, jsonify, request

app = Flask(_name_)

# Example product data
PRODUCTS = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 5.99},
    {"id": 3, "name": "Product 3", "price": 7.99}
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(PRODUCTS)

@app.route("/search", methods=["GET"])
def search_products():
    query = request.args.get("query")
    results = [product for product in PRODUCTS if query.lower() in product["name"].lower()]
    return jsonify(results)

if _name_ == "_main_":
    app.run(debug=True)
