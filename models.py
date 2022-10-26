from flask_sqlalchemy import SQLAlchemy 
# import psycopg2

db=SQLAlchemy()


image_url = 'https://tinyurl.com/demo-cupcake'

def connect_db(app):
    db.app=app
    db.init_app(app)

class Cupcake(db.model):
    __tablename__='cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, default=image_url)

    def dict(self):
        return {
            'id':self.id,
            'flavor':self.flavor,
            'rating':self.rating,
            'size':self.size,
            'image':self.image
        }

# def get_connection(dbname):
#     connect_str = 'dbname={} host="localhost" user="user" password="password"'.format(dbname)
#     return psycopg2.connect(connect_str)