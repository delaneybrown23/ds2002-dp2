from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
# specify a database
db = client.vvz2bg
# specify a collection
collection = db.dataproject2

directory = "data"

for filename in os.listdir(directory):
	with open(os.path.join(directory, filename)) as f:
		print(f)
		try:
			file_data = json.load(f)
		except Exception as e:
			print(e, "error when loading", f)
		if isinstance(file_data, list):
			try:
				collection.insert_many(file_data)
			except Exception as e:
				print(e, "when importing into Mongo")
				continue
		else:
			try:
				collection.insert_one(file_data)
			except Exception as e:
				print(e)
				continue
