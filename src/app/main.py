from src.app import app
from src.app.extensions import db


#  This allows us to use the server without having it online
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

