# import requests
from flask import Flask, render_template, request, jsonify
from models import db, connect_db, Cupcake

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secretCode'

connect_db(app)
# db.create_all()

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/api/cupcakes')
def get_all_data():
    # cupcake = Cupcake.query.all()
    cupcakes = [cupcake.dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes)

@app.route('/api/cupcakes/<int:id>')
def single_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake)

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    data=request.json
    cupcake = Cupcake(
        # flavor=request.form['flavor'], 
        # size=request.form['size'], 
        # rating=request.form['rating']
        # image=request.form['img_url']
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data['image'] or None
    )
    db.session.add(cupcake)
    db.session.commit()

    # return jsonify(cupcake)
    return (jsonify(cupcake=cupcake.dict()),201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH']) 
def update_cupcakes(id):
    data = request.json 
	cupcake = Cupcake.query.get_or_404(id) 
	# cupcake.flavor = request.json('flavor')
    # cupcake.size = request.json('size')
    # cupcake.rating = request.json('rating')
    # cupcake.img = request.json('image')
	# db.session.commit() 
    # return jsonify(cupcake=cupcake) 
    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.dict())
# I don't know where my issue is here  

@app.route('/api/cupcakes/"<int:id>"', methods=['DELETE'])
def delete_cupcake(id): 
	cupcake = Cupcake.query.get_or_404(id) 
	db.session.delete(cupcake) 
	db.session.commit() 
	return jsonify (message='deleted')