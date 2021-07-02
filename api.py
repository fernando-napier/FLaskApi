from flask import Flask
from flask_restful import Resource, Api
from app.hello_world import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/hello_world', '/', '/hello')

if __name__ == '__main__':
    app.run(debug=True)