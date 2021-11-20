from apis.Product import Product
from apis.Scan import Scan
from apis.Statistic import Statistic
from apis.Chart import Chart

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Product,
                 '/product',
                 '/product/<product_id>')

api.add_resource(
    Scan,
    "/scan/<user_id>/<product_id>"
)

api.add_resource(
    Statistic,
    "/statistic/<user_id>",
)

api.add_resource(
    Chart,
    "/chart/<user_id>/<chart_type>"
)

if __name__ == '__main__':
    app.run(debug=True)
