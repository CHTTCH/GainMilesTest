from flask import Flask
from adapter.database import init_db
from adapter.controller.product.product_controller import product_blueprint

app = Flask(__name__)
# For run on loaclhost
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://GainMiles:GainMiles@localhost:5433/gain_miles'

# For docker compose using
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://GainMiles:GainMiles@db:5433/gain_miles'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

app.register_blueprint(product_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
