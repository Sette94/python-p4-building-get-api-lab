#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'


@app.route('/bakeries')
def bakeries():
    bakeries = Bakery.query.all()

    if bakeries:
        bakeries_dict = [bakery.to_dict() for bakery in bakeries]
        make_response = (
            bakeries_dict,
            200
        )

    else:
        make_response = (
            {},
            500
        )

    return make_response


@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakeries = Bakery.query.filter(Bakery.id == id).first()
    if bakeries:
        make_response = (
            bakeries.to_dict(),
            200
        )

    else:
        make_response = (
            {},
            500
        )

    return make_response


@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()

    if baked_goods:
        baked_goods_dict = [baked_good.to_dict() for baked_good in baked_goods]
        make_response = (
            baked_goods_dict,
            200
        )
    else:
        make_response = (
            {},
            500
        )

    return make_response


@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()

    if baked_goods:
        make_response = (
            baked_goods[0].to_dict(),
            200
        )
    else:
        make_response = (
            {},
            500
        )

    return make_response


if __name__ == '__main__':
    app.run(port=5555, debug=True)
