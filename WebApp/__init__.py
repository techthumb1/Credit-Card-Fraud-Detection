from flask import Flask

from WebApp.routes.home_routes import home_routes
from WebApp.routes.feature_routes import feature_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(feature_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)