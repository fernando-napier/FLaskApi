import requests
from flask_restful import Resource
from flask import request

class SelectStations(Resource):
		
	def get(self):
		stations = request.args.get("values")
		stationArray = stations.split(",")
		urlParams = ""
		for x in stationArray:
			urlParams = urlParams + "station=" + x + "&"
		urlParams = urlParams.strip("&")
		url = "https://web-services.unavco.org/metadata/stationlist/sites/beta?" + urlParams
		headers = {"Accept": "application/json"}
		print(url)
		r = requests.get(url, headers=headers)
		print(r.content)
		return r.json()