from flask import Flask

from api import api

app = Flask(__name__)
app.register_blueprint(api)


port_number = 5000
if __name__ == '__main__':
    print(f"Server running on {port_number}")
    app.run(port=port_number)