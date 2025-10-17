from flask import Flask, render_template, request, redirect
from models import db, User, Client

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

@app.route('/clients')
def clients():
    all_clients = Client.query.all()
    return render_template('clients.html', clients=all_clients)

@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = User(
        username=request.form['username'],
        email=request.form['email']
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')

@app.route('/add_client', methods=['POST'])
def add_client():
    new_client = Client(
        company_name=request.form['company_name'],
        contact_person=request.form['contact_person'],
        contact_email=request.form['contact_email']
    )
    db.session.add(new_client)
    db.session.commit()
    return redirect('/clients')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)