from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app(config_name=None):
    app = Flask(__name__)
    
      # Configure database settings based on the environment
    if config_name == "testing":
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"# Use an in-memory DB
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test_db.db' 
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # Ensure tables are created
    
    from routes import register_routes
    register_routes(app,db)
    
    migrate = Migrate(app,db)
    
    return app
    