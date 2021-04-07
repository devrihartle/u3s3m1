"""Main app/routing for assignment"""

from flask import Flask
from assignment.models import DB, User

# creates flask application
def create_app():
    """creating and configuring an instance of the Flask application"""
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #not tracking the modifications

    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template("base.html", title="home", users=User.query.all())

    return app

