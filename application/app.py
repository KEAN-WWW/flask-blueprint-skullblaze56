from flask import Flask
from application.bp.homepage.routes import homepage

# initialize Flask service
app = Flask(__name__, 
           template_folder='templates')  # Add template folder configuration

# register blueprint

# Register blueprints
app.register_blueprint(homepage)

if __name__ == "__main__":
    app.run(debug=True)

