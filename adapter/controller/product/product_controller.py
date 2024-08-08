from flask import Blueprint, request, jsonify
from use_case.product.create_product import CreateProduct
from use_case.product.read_product import ReadProduct
from use_case.product.update_product import UpdateProduct
from use_case.product.delete_product import DeleteProduct

from adapter.repository.product.product_repository import ProductRepository

product_blueprint = Blueprint('product', __name__)
product_repository = ProductRepository()

@product_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.json
    create_use_case = CreateProduct(product_repository)
    new_product = create_use_case.execute(data)
    
    return jsonify({'message': 'Product created', 'product': new_product.id}), 201

@product_blueprint.route('/products', methods=['GET'])
def get_products():
    read_use_case = ReadProduct(product_repository)
    products = read_use_case.get_all()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'code': product.code,
        'category': product.category,
        'size': product.size,
        'unit_price': float(product.unit_price),
        'inventory': product.inventory,
        'color': product.color
    } for product in products])
    
@product_blueprint.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    read_use_case = ReadProduct(product_repository)
    product = read_use_case.get_by_id(id)
    if product:
        return jsonify({
            'id': product.id,
            'name': product.name,
            'code': product.code,
            'category': product.category,
            'size': product.size,
            'unit_price': float(product.unit_price),
            'inventory': product.inventory,
            'color': product.color
        })
    return jsonify({'message': 'Product not found'}), 404

@product_blueprint.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    update_use_case = UpdateProduct(product_repository)
    updated_product = update_use_case.execute(id, data)
    if updated_product:
        return jsonify({'message': 'Product updated'})
    return jsonify({'message': 'Product not found'}), 404

@product_blueprint.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    delete_use_case = DeleteProduct(product_repository)
    result = delete_use_case.execute(id)
    if result:
        return jsonify({'message': 'Product deleted'})
    return jsonify({'message': 'Product not found'}), 404
