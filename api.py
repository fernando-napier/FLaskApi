from flask import Flask
from flask_restful import Resource, Api
from app.HelloWorld.hello_world import HelloWorld
from app.MetaData.metadata import MetaData
from app.MetaData.metadata_all import  MetaDataAll
from app.MetaData.metadata_stations import  MetaDataStations
from app.Stations.all_stations import  AllStations
from app.Stations.select_stations import  SelectStations

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/hello_world', '/', '/hello', '/helloworld')
api.add_resource(MetaData, '/metadata')
api.add_resource(MetaDataAll, '/metadata/all')
api.add_resource(MetaDataStations, '/metadata/<string:stations>')
api.add_resource(AllStations, '/stations/all')
api.add_resource(SelectStations, '/stations')

if __name__ == '__main__':
    app.run(debug=True)