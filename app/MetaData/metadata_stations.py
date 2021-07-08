from flask_restful import Resource
from flask import request

class MetaDataStations(Resource):

	def put(self):
		return {'metadata': 'should update ALL'}
		
	def get(self, stations):
		return {'stations': stations}