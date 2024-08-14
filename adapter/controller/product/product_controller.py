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
    
    return jsonify({
        'id': new_product.id,
        'name': new_product.name,
        'code': new_product.code,
        'category': new_product.category,
        'unit_price': new_product.unit_price,
        'inventory': new_product.inventory,
        'sizes': [size.name for size in new_product.sizes],
        'colors': [color.name for color in new_product.colors]
    }), 201
    # return jsonify({'message': 'Product created', 'product': new_product.id}), 201

@product_blueprint.route('/products', methods=['GET'])
def get_products():
    read_use_case = ReadProduct(product_repository)
    products = read_use_case.get_all()
    if products:
        return jsonify([{
            'id': product.id,
            'name': product.name,
            'code': product.code,
            'category': product.category,
            'sizes': [size.name for size in product.sizes],
            'unit_price': float(product.unit_price),
            'inventory': product.inventory,
            'colos': [color.name for color in product.colors]
        } for product in products])
    else:
        return []
    
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
            'sizes': [size.name for size in product.sizes],
            'unit_price': float(product.unit_price),
            'inventory': product.inventory,
            'colors': [color.name for color in product.colors]
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
