from flask_restful import Resource
from flask import request

class MetaDataAll(Resource):

	def put(self):
		return {'metadata': 'should update ALL'}
		
	def get(self):
		return {'metadata': 'hello all world'}