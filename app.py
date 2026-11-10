from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():
  return jsonify({"message": "Welcome to the Product API!"}) # creates a Python dictionary that gets converted to a JSON respone

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products", methods=["GET"])
def get_products():
  category = request.args.get("category") # grab query parameter
  
  if category:
    filtered_products = [
      product for product in products
      if product["category"].lower() == category.lower()
    ]
    return jsonify(filtered_products)
  return jsonify(products)

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>", method=["GET"])
def get_product_by_id(id):
  for product in products:
    if product["id"] == id:
      return jsonify(product)
  
  return jsonify({"error": "Product not found"}), 404
  
  
if __name__ == "__main__":
  app.run(debug=True)
