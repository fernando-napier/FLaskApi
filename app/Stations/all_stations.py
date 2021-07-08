from flask_restful import Resource
from flask import request

class AllStations(Resource):

	def put(self):
		return {'action': 'should update all stations'}
		
	def get(self):
		return {'action': 'should return all stations'}