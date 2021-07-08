from flask_restful import Resource
from flask import request

class MetaData(Resource):

	def put(self):
		return {'metadata': 'should update'}
		
	def get(self):
		return {'metadata': request.args}