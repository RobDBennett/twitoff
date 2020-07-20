"""Main app/routing file for Twitoff."""
from flask import Flask, render_template
from .models import DB, User, add_test_users

def create_app():
    """Creates and configures an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html')
    
    @app.route('/add_test_users')
    def add_test():
        DB.drop_all()
        DB.create_all()
        add_test_users()
        return 'Users added!'

    @app.route('/view_test_users')
    def view_users():
        users = User.query.all()
        return '\n'.join([str(user) for user in users])
    
    return app
