from flask import Flask, request, render_template, url_for, session,jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema,fields
#from flask_marshmallow import Marshmallow
#from werkzeug.utils import redirect, secure_filename
#from flask_migrate import Migrate

app = Flask(__name__)
app.app_context().push()
#config to data base
USER_DB = 'postgres'
PASS_DB = 'postgres'
URL_DB = 'localhost'
NAME_DB = 'flask_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# object to database
db = SQLAlchemy (app)

#**app.secret_key = 'token_security'

# config  flask - migrate
#**migrate = Migrate()
#**migrate.init_app(app, db)

class User(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    fullname=db.Column(db.String(250),nullable=False)
    email=db.Column(db.String(250),nullable=False)
    password=db.Column(db.String(50),nullable=False)
    #image = db.Column(db.LargeBinary)
    def __repr__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)

    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
class UserSchema(Schema):
    id=fields.Integer()
    fullname=fields.String()
    email=fields.String()
    password=fields.String()  
@app.route('/api/users', methods=['GET'])
def get_all_user():
    user = User.get_all()
    serializer=UserSchema(many=True)
    data = serializer.dump(user)
    return jsonify(
        data
    )
@app.route('/api/users', methods=['POST'])
def load_user():
    data = request.get_json()
    add_user = User(
        fullname = data.get('fullname'),
        email = data.get('email'),
        password = data.get('password')
        )
    add_user.save()
    serializer = UserSchema()
    data=serializer.dump(add_user)
    return jsonify(
        data
    )
@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.get_by_id(id)
    serializer = UserSchema()
    data = serializer.dump(user)
    return jsonify(
        data
    )
    
@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    user_update = User.get_by_id(id)

    data=request.get_json()
    user_update.fullname=data.get('fullname')
    user_update.email=data.get('email')
    user_update.password=data.get('password')
    db.session.commit()
    serializer=UserSchema()
    usr_data =  serializer.dump(user_update)
    return jsonify(usr_data)

@app.route('/api/user/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    usr_to_delete = User.get_by_id(id)
    usr_to_delete.delete()
    return jsonify({"message":"user removed"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)


    #**def __str__(self):
    #**    return (
    #**        f'Id:{self.id},'
    #**        f'Fullname:{self.fullname},'
    #**        f'Email:{self.email},'
    #**        f'Password:{self.password},'
    #**    )

#**@app.route('/test')
#**def users():
#**    all_users = User.all()
#**    return users_schema.dump(all_users)
#**
#**@app.route("/", methods = ['GET', 'POST'])
#**def index():
#**    if 'username' in session:
#**        return render_template('main.html')#(f'Welcome {session["username"]}')
#**    return '''<a href="/login">registrar nuevo usuario</a>'''
#**    #'please register has new user'#render_template('start.html')
#**
#**
#**@app.route('/login', methods=['GET', 'POST'])
#**def login():
#**    if request.method == 'POST':
#**        user = request.form['username']
#**        psw = request.form ['password']
#**        session ['username'] = user
#**
#**        #session['username'] = request.form['username']
#**        return redirect(url_for('index'))
#**    return render_template('start.html')#'''
#**    #    <form method="post">
#**    #        <p><input type=text name=username>
#**    #        <p><input type=submit value=Login>
#**    #    </form>
#**    #'''
#**@app.route ('/logout')
#**def logout():
#**    session.pop('username')
#**    return redirect(url_for('login'))
#**
#**@app.route ('/users', methods =['GET'])
#**def getUsers():
#**    return {"id":"1","name":'edgar',"username": "ae21"}
#**