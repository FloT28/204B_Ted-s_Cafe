from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session



# App Init
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem for server-side sessions
Session(app)

# PostgreSQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1@localhost:5432/tedsCafeDB"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# Home route
@app.route('/', methods=['GET'])
def index():
    return render_template('menu.html')


# Run the app and make it accessible on the network
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

